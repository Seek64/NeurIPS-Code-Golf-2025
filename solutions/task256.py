def p(g):
 w=sum(m:=max(g))//2;i=w+g.index(m)
 for r in g:r[:i]=[2+(i-w|8)//9]*i;i-=i>0
 return g