import re
p=lambda g:[g:=eval(re.sub(r"(?=(.{%d})+([^0]), \2.{%d}\2, 0, (.))0"%(x:=len(g)*3+5,x*2-10),r"\3",str([*zip(*g[::-1])])))for _ in g][3]