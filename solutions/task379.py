import re
S=re.sub
p=lambda g:[g:=eval(S("(2[^)8]*)0, 8, 0",r"*[2]*len([\1]),8,2,8",S("0(?=, 8.{%d}.2)"%len(3*g),"8",f"{*zip(*g[::-1]),}")))for _ in g][7]