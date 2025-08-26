import re
p=lambda g,k=0:[eval(re.sub("[^2]{9}2"*2+"?",lambda m:m[0][::-1],str(l)))for*l,in zip(*k or p(g,g))]