import re
p=lambda g:[*zip(*eval(re.sub(r'0(?=(.{35})+..([^0]).{28}\2, \2)',r'\2',str(g[70:]or p(g*2)))))][::-1]