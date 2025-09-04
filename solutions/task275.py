def p(g):
 l=len(g);a,b=g[:l//2],g[l//2:]
 if'8'in str(a):a,b=b,a
 return[[l//5*k for k in i for l in j]for i in a for j in b]*(l>5)or[*zip(*p([*zip(*g)]))]