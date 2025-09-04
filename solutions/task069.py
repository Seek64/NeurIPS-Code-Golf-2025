R=range(100)
def p(g):
 f=sum(g,[]);P=[[i,f[i]]for i in R if f[i]%8]
 for i in R:
  for j,x in(f[i]==8)*P:f[j],f[i+j-P[0][0]]=0,x
 return[f[i:i+10]for i in R[::10]]