def p(g,i=10):
 for l in g:w=len(l)*2-2;l[min(i:=~-i%w,w-i)]=1
 return g