import os

for task_num in range(1,401):
    path = f"submission/task{task_num:03d}.py"
    
    if os.path.exists(path):
        print(os.path.getsize(path))
    else:
        print()