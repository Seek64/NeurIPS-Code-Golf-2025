import re
p=lambda g:g[57330:]or eval(re.sub('5([^)]*), [^50]',r'5,5\1',str([*zip(*p(2*g)[::-1])])))