import re
p=lambda g:eval(re.sub(r"(?<=([1-9]).{%d})\1(?=.{%d}\1)"%(x:=len(g[0])*3+4,x),"8",str(g)))