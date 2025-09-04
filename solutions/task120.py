import re
p=lambda g:eval(re.sub(r"([^0])(?<=\1.{%d}\d)(?=.{%d}\1)"%(x:=len(g[0])*3+4,x),"8",str(g)))