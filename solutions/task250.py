import re
p=lambda g:[g:=eval(re.sub(f"5(({'.'*n}0)*)(?={'.'*n}2)",r"0\1+5",f"{*zip(*g[::-1]),}"))for n in b'""'*4][-1]