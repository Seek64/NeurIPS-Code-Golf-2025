R=range(11)
p=lambda g:min(({*str(t:=[[[5,g[y//4+p%3*4][x//4+p-p%4]][x%4<3>y%4]for x in R]for y in R])},t)for p in R)[1]