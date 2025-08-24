import re
p=lambda g,n=3:-n*g or[eval(re.sub(r'0(?=.*([^0]), (?!\1|0)(.), 0)',r'\2',str(r)))for*r,in zip(*p(g,n-1)[::-1])]