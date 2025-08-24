import re
p=lambda g,n=-15:g*n or[*zip(*eval(re.sub('0(?=, [47].{25}[47])','7',str(p(g,n+1)[::-1]))))]