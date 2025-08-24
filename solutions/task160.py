import re
p=lambda g,n=0:eval(re.sub(r'(1, 1, 1)(.{26}), 0, 1(.{25})\1',r'0,2,0\2+1,2,2\3 0,2,0',str(n*g or p(g,1))))