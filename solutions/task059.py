R=range(11)
p=lambda g:[[(g[i][j]==5)*5or(max(l:=[sum(sum(r[i%3*4:][:3])for r in g[i//3*4:][:3])for i in R])==l[i//4*3+j//4])*sum({*sum(g,[-5])})for j in R]for i in R]