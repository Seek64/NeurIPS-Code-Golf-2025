import re
p=lambda g,n=-59,a='3|0':n*g or eval(re.sub(a,a[0],str([*zip(*p(g,n+1,r'4|0(?=, 4|[^)]*([^04]), \1)')[::-1])])))