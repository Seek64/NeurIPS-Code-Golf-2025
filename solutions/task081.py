import re
p=lambda g:eval(re.sub('0(?=, 8.{19}8)','1',f"{*zip(*g[49:]or p(g*2)),}"))[::-1]