import re
p=lambda g:exec(fr'g[::-1]=zip(*eval(re.sub(r"(?=(.{{{(x:=len(g)*3)+5}}})+([^0]), \2{".."*x}\2, 0, (.))0",r"\3",str(g))));'*4)or g