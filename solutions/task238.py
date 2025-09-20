def p(p):
 i=p
 for*f,in p*4:i=[f for*f,in zip(*i)if 8in f];p=[f for*f,in zip(*p)if{*f}-{8,0}]
 for n in p[1:-1]:n[1:-1]=i.pop(0)
 for*f,in p*4:i=0;p=[[n%~n&f[0]for n in f[:d]]+f[d:]for*f,in zip(*p[::-1])if[d:=min(i,len(p)-(i:=i+1))]]
 return p