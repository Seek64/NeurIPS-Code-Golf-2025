import re
p=lambda g,n=-3:n*g or p(eval(re.sub("([1-9])((.{32})+?[^)]+?)8",r"0\2\1",str([*zip(*g[::-1])]))),n+1)