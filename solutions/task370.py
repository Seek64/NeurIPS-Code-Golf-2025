import re
def p(g):
 for i in"."*4:
  l=len(g);*g,=zip(*g[::-1]);f=sum(g,());i=f.index;d=i(v:=sum({*f})-f[0])-i(0)
  for _ in(d>d%l<6)*g:g=eval(re.sub(f"(?<=(0|{v}).{{{d*3+2*d//l-39**(d==40)}}})\d","v",str(g)))
 return g