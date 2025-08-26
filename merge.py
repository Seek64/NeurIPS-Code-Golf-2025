import os, shutil, golf_utils

### config options ###

#Set to True and no files will be updated (for testing)
dry_run = False

#directories
source = "my_solutions"
dest = "solutions"

#don't even try zip unless this long (to speed things up)
#not necessary now, but maybe in the future when we have a fancier packer
try_zip_threshhold = 0 

### end of config options ###

def get_packed_source(file):
    if not os.path.exists(file):
        return None, None
    with open(file, "rb") as f:
        data = f.read()
    saved = 0
    if len(data) >= try_zip_threshhold:
        data_packed = golf_utils.pack(data)
        saved = len(data) - len(data_packed)
        if saved > 0:
            data = data_packed
        else:
            saved = 0
    return data, saved

existing_count = 0
new_count = 0
existing_points = 0
new_points = 0
pack_results = {}

for task_num in range(1,401):
    path_in  = f"{source}/task{task_num:03d}.py"
    path_out = f"{dest}/task{task_num:03d}.py" 
    
    source_bytes, pack_save = get_packed_source(path_in)
    if not source_bytes: continue;
    
    source_len = len(source_bytes)
    dest_bytes, _ = get_packed_source(path_out)
    dest_len = len(dest_bytes) if dest_bytes else 2500
        
    if source_len < dest_len:
        saved = dest_len - source_len
        print(f"Task {task_num:03d}: {dest_len} -> {source_len} (+{saved})")
        if pack_save:
            print(f"  packing: {source_len + pack_save} -> {source_len} (+{pack_save})")
        
        existing_count += dest_len < 2500
        new_count += dest_len == 2500
        existing_points += (dest_len < 2500) * saved
        new_points += (dest_len == 2500) * saved
        
        if not dry_run:
            shutil.copy(path_in, path_out)
        

print(f"New solutions: {new_count}, {new_points} points")
print(f"Existing solutions: {existing_count}, {existing_points} points")
print(f"Total: {new_count + existing_count} improvements, {new_points + existing_points} points")