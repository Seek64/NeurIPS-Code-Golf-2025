R=range(10)
p=lambda g:[[g[i][j]*~(3*sum([[0,*a]for a in(10*[0],*g)][i:i+3],[0]))[j+3::11].count(5)%13for j in R]for i in R]