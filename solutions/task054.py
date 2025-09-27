import re
def p(i):
 f=sum(i,[]);r,l,m,*z={}.fromkeys((9*f[1:])[7::30]+f[240:])
 for k in[k for k in range(838)if(f[k+62]==m)and({*f[k+61:k+64]}&{r,l}or(p:=k))]+[p]:
  for n in range(25):i[k//30+n//5][k%30+n%5]=r*(k==p)or(f[n//5*30+n%5+k],f[n//5*30+n%5+p])[f[n//5*30+n%5+p]!=r!=l==f[n//5*30+n%5+k]]
 return[i:=eval(re.sub(f"{l}, (?=([^{r}], )\\1+{m})","\\1",f"{*zip(*i[::-1]),}"))for n in f][63]