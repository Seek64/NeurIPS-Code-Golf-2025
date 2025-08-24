import re
p=lambda g,n=-15:g*n or[*zip(*eval(re.sub('0(?=, 8.{19}8)','1',str(p(g,n+1)[::-1]))))]