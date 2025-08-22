source = "solutions"

from zlib import compress

def zip_src(src):
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

 return b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + \
  delim + compressed + delim + \
  b',"L1")))'


import os

total_save = 0

submission = "submission"

os.makedirs(submission, exist_ok=True)

for task_num in range(1, 401):
    path_in = f"{source}/task{task_num:03d}.py"
    path_out = f"{submission}/task{task_num:03d}.py"

    if not os.path.exists(path_in): continue

    with open(path_in, "rb") as task_in:
        task_src = task_in.read()

    zipped_src = zip_src(task_src)

    improvement = len(task_src) - len(zipped_src)

    if improvement > 0:
        task_src = zipped_src
        total_save += improvement

    with open(path_out, "wb") as task_out:
        task_out.write(task_src)

print(f"Saved {total_save}b with zlib")

import zipfile

with zipfile.ZipFile(f"{submission}.zip", "w") as zipf:
 for task_num in range(1, 401):
  task_id = f"{task_num:03d}"
  src_path = f"{submission}/task{task_id}.py"
  if os.path.exists(src_path):
   zipf.write(src_path, arcname=f"task{task_id}.py")