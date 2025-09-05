import re
p=lambda g,n=-35:n*g or eval(re.sub("([^20]), 2(.{28})0",r"\1,\1,\1\2\1,2",str([*zip(*p(g,n+1)[::-1]),[0]*9])))[:9]