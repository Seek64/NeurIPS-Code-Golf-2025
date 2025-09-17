import re
p=lambda g:g[150:]or eval(re.sub('1..1..1(.{25}).{6}[12]',r'0,2,0\1 2,2,2',str(p(g*2)[::-1])))