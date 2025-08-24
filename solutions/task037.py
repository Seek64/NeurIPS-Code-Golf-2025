import re
p=lambda g,n=23:-n*g or[*zip(*eval(re.sub(r'(([^0]).{34})(?=(0.{34})+\2)',r'\1\2+',str(p(g,n-1)[::-1]))))]