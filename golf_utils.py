from zlib import compress as compress1
from zopfli.zlib import compress as compress2


def pack(src: bytes):
    """Given a python program as a bytes object, returns a possibly shorter python program"""

    def sanitize(b_in: bytes, delim: bytes):
        """Clean up problematic bytes in compressed b-string"""
        b_out = bytearray()
        for b, b_next in zip(b_in, [*b_in[1:], 0]):
            if b == 0:
                if b_next in b"0123456789abcdef":
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
    for i in range(10):
        compressed.append(compress2(src, numiterations=1 << i))
    for compression_level in range(-1, 10):
        compressed.append(compress1(src, compression_level))

    for c in compressed:
        for delim in [b"'", b'"', b"'''"]:
            codes.append(
                b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
                + delim
                + sanitize(c, delim)
                + delim
                + b',"L1")))'
            )

    return min(codes, key=len)
