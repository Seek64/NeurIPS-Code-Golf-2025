import re
p=lambda g:g[150:]or eval(re.sub("([1-9])((.{32})+?[^)]+?)8",r"0\2\1",f"{*zip(*p(g*2)[::-1]),}"))