import os

with open("scores.txt") as f:
    entries = f.read().split("\n")
total = 0
for i in range(1, 401):
    try:
        score = os.path.getsize(f"../submission/task{i:03}.py")
        total += 2500 - score
        print(f"task{i:03}:", score)
        #if score != int(entries[i-1]):
        #    print("MISMATCH!")
    except FileNotFoundError:
        pass

print("Total score:", total)