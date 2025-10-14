R=range(10)
p=lambda g:[[(o:=g[y][x])*(o!=5)or(sum((g[Y]+g*2)[x+i-y-3+Y]==5for i in b""for Y in R)==1)*sum({*max(g)}-{5})for x in R]for y in R]