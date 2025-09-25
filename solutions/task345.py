import re
p=lambda g:eval(re.sub("(?=0.{31}2)|(?<=5.{31}2,)","2|",str(g[5110:]or p(g*2))))