import re
p=lambda g,n=39:-n*g or eval(re.sub(r'(([^0]).{34})(?=(0.{34})+\2)',r'\1\2+',str(p(g,n-1)[::-1])))