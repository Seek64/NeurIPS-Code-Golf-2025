import re
p=lambda g,n=-7:g*n or[eval(re.sub('(2), 0(.*)(, 3)|(1), 0(.*)(, 7)',r'\1\3\2\4\6\5,0',str(r)))for*r,in zip(*p(g,n+1)[::-1])]