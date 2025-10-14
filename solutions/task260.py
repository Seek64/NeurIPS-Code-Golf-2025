R=range
p=lambda g:[[g[y][x]**5%415%10or(sum((g[i//5]+g*2)[x-y+i%5-2+i//5]==5for i in R(50))==1)*sum({*max(g)}-{5})for x in R(10)]for y in R(10)]