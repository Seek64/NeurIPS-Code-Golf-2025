import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub(r"(?=(.{%d}.{5})+([^0]), \2.{%d}\2, 0, (.))0"%(x:=len(g)*3,x*2),r"\3",str(g))));'*4)or g