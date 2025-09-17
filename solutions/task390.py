import re
p=lambda g,k=0:eval(re.sub("[^(2]{9}2"*2+"?","*[\g<0>][::-1]",f"{*zip(*k or p(g,g)),}"))