import re
p=lambda g,n=3:-n*g or p(eval(re.sub(r"0(?=[^)]*([^0]), ((?!\1|0).), 0)",r"\2",str([*zip(*g[::-1])]))),n-1)