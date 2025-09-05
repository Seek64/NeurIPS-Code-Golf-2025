import re
p=lambda g:eval(re.sub(r"(?<=([^0]).{34})(?=(.{35})*\1)0",r"\1",str(g[10230:]or p(g*2)[::-1])))