E=enumerate
p=lambda g,i=-1:[[sum({*sum(g*x,[-x])})or p(c*2,i)|p(r*2,j)for j,(*c,x)in E(zip(*g,r))]for i,r in E(g*-i)]or g[i+1]|g[i-1]or g.count(0)%-len(g)%3*(g[i+2]|g[i-2])