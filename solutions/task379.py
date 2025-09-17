import re
S=re.sub
p=lambda g,n=-7:n*g or p(eval(S("(2[^)8]*)0, 8, 0",r"*[2]*len([\1]),8,2,8",S("0(?=, 8.{%d}.2)"%(len(g)*3),"8",f"{*zip(*g[::-1]),}"))),n+1)