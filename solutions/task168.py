import re
p=lambda g,n=-3:g*n or[*zip(*eval(re.sub(r'0(?=(.{35})+..([^0]).{28}\2, \2)',r'\2',str(p(g,n+1)[::-1]))))]