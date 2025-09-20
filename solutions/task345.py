import re
p=lambda g:eval(re.sub("0(?=.{31}2)|(?<=5.{31}2, )0","2",str(g[81910:]or p(g*2))))