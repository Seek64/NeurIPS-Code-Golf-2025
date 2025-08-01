from test_cases import tests
from task007 import p

print(all(p(test["input"]) == test["output"] for test in tests["arc-gen"]))