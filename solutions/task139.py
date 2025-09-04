import re
p=lambda g:g[36855:]or[*zip(*eval(re.sub('0(?=, [47].{25}[47])','7',str(p(g*2)))))][::-1]