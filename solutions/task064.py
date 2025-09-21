import re
p=lambda g:[g:=eval(re.sub(f"{a,b}(?={e}*[^{a,b}])","a,a",f"{*zip(*g[::-1]),}"))for a,*e,b in[sorted(sum(g,[]),key=sum(g,g).count)]*56][-1]