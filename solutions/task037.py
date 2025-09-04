import re
p=lambda g,n=-9:n*g or eval(re.sub(r"(?<=([^0]).{34})(?=(.{35})*\1)0",r"\1",str(p(g,n+1)[::-1])))