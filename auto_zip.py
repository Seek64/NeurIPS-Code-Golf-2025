import os, golf_utils

source = "solutions"
submission = "submission"

total_save = 0
min_pack_length = 200

os.makedirs(submission, exist_ok=True)

for task_num in range(1, 401):
    path_in = f"{source}/task{task_num:03d}.py"
    path_out = f"{submission}/task{task_num:03d}.py"

    if not os.path.exists(path_in): continue

    with open(path_in, "rb") as task_in:
        task_src = task_in.read()

    if len(task_src) >= min_pack_length:
        zipped_src = golf_utils.pack(task_src)

        improvement = len(task_src) - len(zipped_src)

        if improvement > 0:
            print(f"Task {task_num:03d}: {len(task_src)} -> {len(zipped_src)} (+{improvement})")
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