import re
s=", 0(.{22})0, "
p=lambda g:[g:=eval(re.sub(f"0, 0{s}5{s}0, 0",r"5,1,5\1 1,0,1\2 5,1,5","%s"%g))for _ in g][2]