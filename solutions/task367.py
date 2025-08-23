e=enumerate
def p(g):
 for i,r in e(g):
  for j,x in e(r):exec("B=T=i;R=j+1\nwhile[]<r[R:]<[1]:R+=1\nwhile~-any([*g,g*9][B][j:R]):B+=1\nwhile~x&(c:=lambda a,b=j,c=R,h=g:1-(0<=a<len(h))or((H:=[1,1,*h[a],1,1])[b]<2>H[c+3])&all(H[b+1:c+2]))(i-1)&c(B)&c(j-1,i,B,h:=[*zip(*g)])&c(R,i,B,h)&(T<B):g[T][j:R]=[4]*(R-j);T+=1")
 return g