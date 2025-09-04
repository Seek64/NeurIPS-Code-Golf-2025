import re
p=lambda g:eval(re.sub('0((.{34}(1)){2})|(((2).{34}){2})0',r'\3\1\4\6',str(g[5110:]or p(g*2))))