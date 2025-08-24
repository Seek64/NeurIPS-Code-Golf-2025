import re
p=lambda g,n=-19:n*g or eval(re.sub('(5[^)]*(1), 0|5[^)]*0(?=, (2)))',r'\1+\2\3',str([*zip(*p(g,n+1)[::-1])])))