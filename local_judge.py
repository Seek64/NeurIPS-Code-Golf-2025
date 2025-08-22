import os
import importlib

TASK = 1
N_TESTS = 100

os.system(f"py ARC-GEN/arc_gen.py generate {TASK} {N_TESTS} > tests.txt")
with open("tests.txt") as f:
    test_cases = eval(f.read())
os.remove("tests.txt")

sol = importlib.import_module(f"submission.task{TASK:03}")

print(f"Testing task{TASK:03}:")
if all(sol.p(test["input"]) == test["output"] for test in test_cases):
    print("SUCCESS!")
else:
    print("FAIL!")
