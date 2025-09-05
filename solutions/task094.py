import re
p=lambda g:g[225:]or[*zip(*eval(re.sub("8(?=(.{47})*, 1, 1, [86])","6",str(p(g*2)))))][::-1]