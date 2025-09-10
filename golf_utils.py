import zlib
import zopfli.zlib
import deflate

from reencoder import reencode


def pack(src: bytes):
    """Given a python program as a bytes object, returns a possibly shorter python program"""

    def sanitize(b_in: bytes, delim: bytes):
        """Clean up problematic bytes in compressed b-string"""
        b_in = reencode(b_in, delim)
        b_out = bytearray()
        for b, b_next in zip(b_in, [*b_in[1:], 0]):
            if b == 0:
                if b_next in b"01234567":
                    b_out += b"\\x00"
                else:
                    b_out += b"\\0"
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

    codes = [src]

    compressed: list[bytes] = []

    # Standard zlib attempts
    for level in range(-1, 10):
        compressed.append(zlib.compress(src, level=level, wbits=-10))

    # Zopfli attempts
    for i in range(10):
        compressed.append(zopfli.zlib.compress(src, numiterations=1 << i)[2:-4])

    # deflate (libdeflate) attempts
    for level in range(1, 13):
        compressed.append(deflate.deflate_compress(src, compresslevel=level))

    # Wrap compressed bytes in Python exec statements
    for compressed_code in compressed:
        for delim in [b"'", b'"', b"'''"]:
            codes.append(
                b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
                + delim
                + sanitize(compressed_code, delim)
                + delim
                + b',"L1"),~9))'
            )

    # Return the shortest
    return min(codes, key=len)
