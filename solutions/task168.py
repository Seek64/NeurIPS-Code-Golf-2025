import re
p=lambda g:eval(re.sub(r'0(?=(.{35})+.(.[^0]).{27}\2,\2)',r'\2',f"{*zip(*g[70:]or p(g*2)),}"))[::-1]