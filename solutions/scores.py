for i in range(1, 401):
    try:
        with open(f"../submission/task{i:03}.py") as f:
            print(f"task{i:03}:", len(f.read()))
    except FileNotFoundError:
        pass