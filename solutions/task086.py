E=enumerate
p=lambda g,i=-1:i<0and[[sum({*sum(g*x,[-x])})or p(c,i)|p(r,j)for j,(*c,x)in E(zip(*g,r))]for i,r in E(g)]or(s:=g*2)[i+1]|s[i-1]or(len(g)-g.count(0))%3*(s[i+2]|s[i-2])