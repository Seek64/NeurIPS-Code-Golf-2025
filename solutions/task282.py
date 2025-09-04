import re
p=lambda g:eval(re.sub('0, ([^0]), 0',r'2^\1,78%\1,2^\1',str([*zip(*g[9:]or p(g*2))])))