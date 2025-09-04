E=enumerate
o=lambda r,i:(s:=r*2)[i+1]|s[i-1]or(len(r)-r.count(0))%3*(s[i+2]|s[i-2])
p=lambda g:[[sum({*sum(g*x,[-x])})or o(c,i)|o(r,j)for j,(*c,x)in E(zip(*g,r))]for i,r in E(g)]