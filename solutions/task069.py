R=range(320)
def p(g):
 *f,=U=b'%r'%g;P=[i for i in R if 88%f[i]%8]
 for i in R:
  for j in(f[i]==56)*P:f[j],f[i+j-P[0]]=48,U[j]
 return eval(bytes(f))