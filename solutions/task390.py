import re
p=lambda g,h=0:[eval(re.sub("[^2]{9}2"*2+"?",lambda s:s[0][::-1],str(r)))for r in zip(*h or p(g,g))]