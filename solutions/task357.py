def p(g,i=10):
 for l in g:x=len(l);w=x*2-2;l[:]=[8]*x;l[min(i:=~-i%w,w-i)]=1
 return g