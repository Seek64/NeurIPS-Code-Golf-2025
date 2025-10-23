import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub(r"0(.{34}([^0]).*)(.)(,.{33}\2)",r"\3\1 0\4",str(g))));'*4)or g