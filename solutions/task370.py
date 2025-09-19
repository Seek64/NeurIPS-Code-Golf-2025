import re
def p(g):
 for i in"."*4:
  l=len(g);*g,=zip(*g[::-1]);f=sum(g,());i=f.index;x=i(0);y=i(v:=sum({*f})-f[0]);d=y-x
  for _ in(d>y%l-x%l)*g:g=eval(re.sub(f"(?<=(0|{v}).{{{d*3+2*d//l-39**(d==40)}}})\d","v",str(g)))
 return g