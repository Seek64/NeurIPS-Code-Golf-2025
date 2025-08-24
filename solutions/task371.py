import re
p=lambda g,n=3:g*-n or[*zip(*eval(re.sub(r'(1(.*)).{6}(0\2(1))|, 7,',r'\1+3,3\4%8,3+\3',str(p(g,n-1)))))]