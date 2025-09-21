import os, golf_utils, zipfile
from multiprocessing import Pool, cpu_count

source = "solutions"
submission = "submission"

min_pack_length = 200
os.makedirs(submission, exist_ok=True)

def process_task(task_num: int):
    path_in = f"{source}/task{task_num:03d}.py"
    path_out = f"{submission}/task{task_num:03d}.py"

    if not os.path.exists(path_in):
        return 0

    with open(path_in, "rb") as task_in:
        task_src = task_in.read()

    improvement = 0
    if len(task_src) >= min_pack_length:
        zipped_src = golf_utils.pack(task_src)
        difference = len(task_src) - len(zipped_src)
        if difference > 0:
            improvement = difference
            print(f"Task {task_num:03d}: {len(task_src)} -> {len(zipped_src)} (+{improvement})")
            task_src = zipped_src

    with open(path_out, "wb") as task_out:
        task_out.write(task_src)

    return improvement

if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        improvements = pool.map(process_task, range(1, 401))

    total_save = sum(improvements)
    print(f"Saved {total_save}b with zlib")

    with zipfile.ZipFile(f"{submission}.zip", "w") as zipf:
        for task_num in range(1, 401):
            src_path = f"{submission}/task{task_num:03d}.py"
            if os.path.exists(src_path):
                zipf.write(src_path, arcname=f"task{task_num:03d}.py")
