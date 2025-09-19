import re
p=lambda g:[g:=eval(re.sub(r"0(.{34}([^0]).*)(.)(,.{33}\2)",r"\3\1 0\4",f"{*zip(*g[::-1]),}"))for _ in g][3]