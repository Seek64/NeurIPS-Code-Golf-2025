from zlib import compress

def pack(src):
    """Given a python program as a bytes object, returns a possibly shorter python program"""
    
    compression_level = 9 # Max Compression

    # We prefer that compressed source not end in a quotation mark
    while (compressed := compress(src, compression_level))[-1] == ord('"'): src += b"#"

    def sanitize(b_in):
        """Clean up problematic bytes in compressed b-string"""
        b_out = bytearray()
        for b in b_in:
            if   b==0:         b_out += b"\\x00"
            elif b==ord("\r"): b_out += b"\\r"
            elif b==ord("\\"): b_out += b"\\\\"
            else: b_out.append(b)
        return b"" + b_out

    compressed = sanitize(compressed)

    delim = b'"""' if ord("\n") in compressed or ord('"') in compressed else b'"'

    compressed = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + \
        delim + compressed + delim + \
        b',"L1")))'
  
    if len(compressed) < len(src):
        return compressed
    else:
        return src