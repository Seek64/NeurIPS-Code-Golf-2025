from task355.test_cases import tests
from task355.task355 import p

print(all(p(test["input"]) == test["output"] for test in tests[:30]))