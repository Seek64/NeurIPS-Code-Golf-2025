R=range(10)
p=lambda g:[g:=[[(g[i][j],n)[i*j>0<n==g[i-1][j-1]and n in sum(g,[])[i*10+j::11]]for j in R][::-1]for i in R]for n in[0,*R]*10][-1]