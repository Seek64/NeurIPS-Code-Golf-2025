import re
p=lambda g:g[57330:]or eval(re.sub("[^05],([0, ]*5)",r"\1,5",f"{*zip(*p(2*g)[::-1]),}"))