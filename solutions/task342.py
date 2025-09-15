import re
p=lambda g:[g:=eval(re.sub("([1-9])((.{32})+?[^)]+?)8",r"0\2\1",str([*zip(*g[::-1])])))for _ in g][3]