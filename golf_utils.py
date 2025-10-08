import zopfli.zlib
import deflate

from reencoder import reencode

ZOPFLI_ITERS = [2048]
DEFLATE_LEVELS = range(7, 13)
DELIMS = [b"'", b'"']

# ZOPFLI_ITERS = [1 << i for i in range(10)]
# DEFLATE_LEVELS = range(1, 13)
# DELIMS = [b"'", b'"', b"'''"]


def sanitize(b_in: bytes, delim: bytes) -> bytes:
    """Clean up problematic bytes in compressed b-string"""
    b_in = reencode(b_in, delim)
    b_out = bytearray()
    for b, b_next in zip(b_in, [*b_in[1:], 0]):
        if b == 0:
            b_out += b"\\x00" if b_next in b"01234567" else b"\\0"
        elif b == ord("\r"):
            b_out += b"\\r"
        elif b == ord("\\") and b_next in b"\0\n\r\"'01234567NU\\abfnrtuvx":
            b_out += b"\\\\"
        elif b == ord("\n") and len(delim) == 1:
            b_out += b"\\n"
        elif bytes([b]) == delim:
            b_out += b"\\" + delim
        else:
            b_out.append(b)
    return bytes(b_out)


def compress(src: bytes) -> bytes:
    """Given a bytes object, returns a zlib compressed literal"""
    compressed: list[bytes | bytearray] = []

    # Zopfli attempts
    for i in ZOPFLI_ITERS:
        compressed.append(zopfli.zlib.compress(src, numiterations=i)[2:-4])  # type: ignore[reportUnknownArgumentType]
    # deflate (libdeflate) attempts
    for level in DEFLATE_LEVELS:
        compressed.append(deflate.deflate_compress(src, compresslevel=level))  # type: ignore[reportUnknownArgumentType]

    literals: list[bytes] = []
    for data in compressed:
        for delim in DELIMS:
            literals.append(delim + sanitize(data, delim) + delim)

    return min(literals, key=len)


def pack(src: bytes) -> bytes:
    """Given a python program as a bytes object, returns a possibly shorter python program"""
    codes = []

    codes.append(
        b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
        + compress(src)
        + b',"L1"),~9))'
    )

    if src.startswith(b"import"):
        imports = src.split()[1]
        codes.append(
            b"#coding:L1\nimport zlib,"
            + imports
            + b"\nexec(zlib.decompress(bytes("
            + compress(src[len(imports) + 8:])
            + b',"L1"),~9))'
        )

    return min(codes, key=len)
