import re
def p(g):a,*_,b=sorted(f:=sum(g,[]),key=f.count);exec(f'g[:]=zip(*eval(re.sub("{a}, {b}(?=[^])]* [^{a}{b}])","a,a",str(g)))[::-1]);'*56);return g