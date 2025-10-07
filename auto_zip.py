from typing import MutableMapping

import os, golf_utils, zipfile, json
from multiprocessing import Pool, cpu_count, Manager

source = "solutions"
submission = "submission"

min_pack_length = 200
os.makedirs(submission, exist_ok=True)


def process_task(task_num: int, zopfli_settings: MutableMapping[int, dict[str, int]]):
    path_in = f"{source}/task{task_num:03d}.py"
    path_out = f"{submission}/task{task_num:03d}.py"

    if not os.path.exists(path_in):
        return 0

    with open(path_in, "rb") as task_in:
        task_src = task_in.read()

    improvement = 0
    if len(task_src) >= min_pack_length:
        if task_num in zopfli_settings:
            best_zopfli_seed = zopfli_settings[task_num]["seed"]
            best_zopfli_iters = zopfli_settings[task_num]["iters"]
        else:
            best_zopfli_seed, best_zopfli_iters = golf_utils.find_best_zopfli_settings(
                task_src
            )
            zopfli_settings[task_num] = {
                "seed": best_zopfli_seed,
                "iters": best_zopfli_iters,
            }

        zipped_src = golf_utils.pack(task_src, best_zopfli_seed, best_zopfli_iters)
        difference = len(task_src) - len(zipped_src)
        if difference > 0:
            improvement = difference
            print(
                f"Task {task_num:03d}: {len(task_src)} -> {len(zipped_src)} (+{improvement})"
            )
            task_src = zipped_src

    with open(path_out, "wb") as task_out:
        task_out.write(task_src)

    return improvement


if __name__ == "__main__":
    manager = Manager()
    zopfli_settings: MutableMapping[int, dict[str, int]] = manager.dict()

    try:
        with open("zopfli_settings.json", "r") as f:
            for k, v in json.load(f).items():
                zopfli_settings[int(k)] = v
    except FileNotFoundError:
        pass

    with Pool(4) as pool:
        improvements = pool.starmap(
            process_task, [(task_num, zopfli_settings) for task_num in range(1, 401)]
        )

    total_save = sum(improvements)
    print(f"Saved {total_save}b with zlib")

    with open("zopfli_settings.json", "w") as f:
        json.dump(dict(zopfli_settings), f)

    with zipfile.ZipFile(f"{submission}.zip", "w") as zipf:
        for task_num in range(1, 401):
            src_path = f"{submission}/task{task_num:03d}.py"
            if os.path.exists(src_path):
                zipf.write(src_path, arcname=f"task{task_num:03d}.py")
