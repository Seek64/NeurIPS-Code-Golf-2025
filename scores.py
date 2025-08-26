import os

solutions = 0
points = 0

for task_num in range(1,401):
    path = f"submission/task{task_num:03d}.py"
    
    if os.path.exists(path):
        byte_length = os.path.getsize(path)
        print(byte_length)
        points += max(1, 2500 - byte_length)
        solutions += 1
    else:
        print()
        
print(f"{solutions}/400 solutions")
print(points, "points")
