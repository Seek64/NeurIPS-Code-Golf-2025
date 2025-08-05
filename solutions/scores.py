with open("scores.txt") as f:
    entries = f.read().split("\n")
for i in range(1, 401):
    try:
        with open(f"../submission/task{i:03}.py") as f:
            score = len(f.read())
            print(f"task{i:03}:", score)
            #if score != int(entries[i-1]):
            #    print("MISMATCH!")
    except FileNotFoundError:
        pass