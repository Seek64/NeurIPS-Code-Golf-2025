import re
p=lambda g:[g:=eval(re.sub("0,(?=.{%d}[^0]) [^0]"%len(3*g),"4,4",f"{*zip(*g[::-1]),}"))for _ in g][3]