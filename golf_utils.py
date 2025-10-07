import zopfli.zlib
import deflate
import random

from reencoder import reencode

random.seed(0)
ZOPFLI_SEEDS = [2 << 32 | 1] + [random.getrandbits(64) for _ in range(256)]
ZOPFLI_ITERS = [2048]
DEFLATE_LEVELS = list(range(7, 13))
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
        elif b == ord("\\") and b_next in b"01234567abfxnrtvuUN'\"\\":
            b_out += b"\\\\"
        elif b == ord("\n") and len(delim) == 1:
            b_out += b"\\n"
        elif bytes([b]) == delim:
            b_out += b"\\" + delim
        else:
            b_out.append(b)
    return bytes(b_out)


def find_best_zopfli_settings(src: bytes) -> tuple[int, int]:
    best_settings = ZOPFLI_SEEDS[0], ZOPFLI_ITERS[0]
    best_length = len(src)

    for seed in ZOPFLI_SEEDS:
        for i in ZOPFLI_ITERS:
            length = len(pack(src, zopfli_seed=seed, zopfli_iters=i, deflate_levels=[]))  # type: ignore[reportUnknownArgumentType]

            if length < best_length:
                best_settings = seed, i
                best_length = length

    return best_settings


def compress(src: bytes, zopfli_seed: int = ZOPFLI_SEEDS[0], zopfli_iters: int = ZOPFLI_ITERS[0], deflate_levels: list[int] = DEFLATE_LEVELS) -> bytes:
    """Given a bytes object, returns a zlib compressed literal"""
    compressed: list[bytes] = []

    # Zopfli attempts
    compressed.append(zopfli.zlib.compress(src, numiterations=zopfli_iters, seed=zopfli_seed)[2:-4])  # type: ignore[reportUnknownArgumentType]
    # deflate (libdeflate) attempts
    for level in deflate_levels:
        compressed.append(deflate.deflate_compress(src, compresslevel=level))  # type: ignore[reportUnknownArgumentType]

    literals: list[bytes] = []
    for data in compressed:
        for delim in DELIMS:
            literals.append(delim + sanitize(data, delim) + delim)

    return min(literals, key=len)


def pack(src: bytes, zopfli_seed: int = ZOPFLI_SEEDS[0], zopfli_iters: int = ZOPFLI_ITERS[0], deflate_levels: list[int] = DEFLATE_LEVELS) -> bytes:
    """Given a python program as a bytes object, returns a possibly shorter python program"""
    if src.startswith(b"import"):
        imports = src.split()[1]
        packed = (
            b"#coding:L1\nimport zlib,"
            + imports
            + b"\nexec(zlib.decompress(bytes("
            + compress(src[len(imports) + 8:], zopfli_seed, zopfli_iters, deflate_levels)
            + b',"L1"),~9))'
        )
    else:
        packed = (
            b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
            + compress(src, zopfli_seed, zopfli_iters, deflate_levels)
            + b',"L1"),~9))'
        )

    if len(packed) > len(src):
        return src
    
    return packed
