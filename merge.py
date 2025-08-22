import os, shutil

source = "submission"
dest = "../NeurIPS-Code-Golf-2025/submission"

existing_count = 0
new_count = 0
existing_points = 0
new_points = 0

for task_num in range(1,401):
    path_in  = f"{source}/task{task_num:03d}.py"
    path_out = f"{dest}/task{task_num:03d}.py" 
    
    if not os.path.exists(path_in):continue
    
    source_len = os.path.getsize(path_in)
    
    if not os.path.exists(path_out):
        dest_len = 2500
    else:
        dest_len = os.path.getsize(path_out)
        
    if source_len < dest_len:
        saved = dest_len - source_len
        print(f"Task {task_num:03d}: {dest_len} -> {source_len} (+{saved})")
        existing_count += dest_len < 2500
        new_count += dest_len == 2500
        existing_points += (dest_len < 2500) * saved
        new_points += (dest_len == 2500) * saved
        
        shutil.copy(path_in, path_out)
        

print(f"New solutions: {new_count}, {new_points} points")
print(f"Existing solutions: {existing_count}, {existing_points} points")
print(f"Total: {new_count + existing_count} improvements, {new_points + existing_points} points")

    