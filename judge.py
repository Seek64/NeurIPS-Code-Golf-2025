import argparse
import json
import os
import time
from multiprocessing import Pool, cpu_count

SOLUTIONS = os.path.join(os.path.dirname(__file__), "solutions")
TASKS = os.path.join(os.path.dirname(__file__), "tasks")

MIN_REPORT = 5.0


def judge(task_num: int):
    solution = f"{SOLUTIONS}/task{task_num:03d}.py"
    if not os.path.exists(solution):
        return
    code = open(solution, "rb").read()

    task = json.load(open(f"{TASKS}/task{task_num:03d}.json"))
    tests = sum(task.values(), [])

    start = time.process_time()

    try:
        scope = {}
        exec(code, scope)
        p = scope["p"]
    except Exception:
        return

    for test in tests:
        try:
            p(test["input"])
        except Exception:
            pass

    elapsed = time.process_time() - start
    if MIN_REPORT < elapsed:
        print(f"Task {task_num:03d}: {elapsed:.3f}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--jobs", default=cpu_count(), type=int)
    parser.add_argument("range", nargs="?", default="1-400", type=str)
    args = parser.parse_args()

    if "-" in args.range:
        start, end = map(int, args.range.split("-"))
    else:
        start = end = int(args.range)

    with Pool(args.jobs) as pool:
        pool.map(judge, range(start, end + 1))


if __name__ == "__main__":
    main()
