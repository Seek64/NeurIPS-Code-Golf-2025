import re
S=re.sub
p=lambda g:[g:=eval(S("0, 8, ([ 0,]+)2",r"1,2,1,*[2]*len([\1])",S("0, 1, .","8,8,8",f"{*zip(*g[::-1]),}")))for _ in g][7]