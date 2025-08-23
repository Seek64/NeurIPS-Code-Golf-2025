import re
def p(g,i=18,c=1):
 while i:i-=1;s,n=re.subn("5"+i//2*", 5",f"{c}"+i//2*f",{c}",f"{[*zip(*g)]}");g=eval(s);c=(c+3*n)%5
 return g