E=enumerate
p=lambda g:[[x*(sum(sum([0,*s][j:j+3])for s in[[],*g][i:i+3])>x)for j,x in E(r)]for i,r in E(g)]