import re
p=lambda g:[g:=eval(re.sub(r"(?=(.{%d}.{5})+([^0]), \2.{%d}\2, 0, (.))0"%(x:=len(g)*3,x*2),r"\3",f"{*zip(*g[::-1]),}"))for _ in g][3]