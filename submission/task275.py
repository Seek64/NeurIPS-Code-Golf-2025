def p(g):
 h,*p=len(g),;N=3+h%7%3;R,*c=range(N*N),
 for i in range(N):c+=g[i][:N];p+=(5>h)*g[i][N:]or g[N+i]
 if 8in c:p,c=c,p
 return[[p[i%N*N+j%N]%7*c[i//N*N+j//N]for j in R]for i in R]