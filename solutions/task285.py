import re
def p(g,n=7):
 for m in re.finditer(r"([1-9]), (?!\1|0)(.)",str(g)):
  i,l=m.start(2),len(g[0])*3+2;s=[(i//l,b:=i%l//3)]
  for c,d in s:*g[c],=g[c];g[c][b+b-d-1]=int(m[1]);s+=[(i,j)for u in range(9)if((g*2)[i:=c+u//3-1]*2)[j:=d+u%3-1]==int(m[2])>0==g[i][b+b-j-1]]
 return-n*g or p([*zip(*g[::-1])],n-1)