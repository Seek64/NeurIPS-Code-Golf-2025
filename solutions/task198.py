import re
p=lambda g,n=-59,a='3|0':n*g or p(eval(re.sub(a,a[0],f"{*zip(*g[::-1]),}")),n+1,r'4|3(?=, 4|[^)]*([^34]), \1)')