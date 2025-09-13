import re
p=lambda g:[g:=eval(re.sub(r"0(?=[^)]*([^0]), ((?!\1|0).), 0)",r"\2",str([*zip(*g[::-1])])))for _ in g][3]