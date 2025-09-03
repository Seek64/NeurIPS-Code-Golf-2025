R=range(32)
def p(g,*l):
 g=[*map(list,zip(*g))];b=[r.count(2)for r in g]+[3]
 for i in R:
  z=i<16;i%=16;r=[*g,g][i]
  if 5in r:l+=r[:],
  elif n:=len(l):
   for j in R:
    j=-~j%(16-n);o=min(q:={y.index(5)-x for x,y in zip(b[j:],l)})
    if(b[j+n]>2)*any(3>[*x,0].index(0)for x in g[j:j+n])*3-len(q)>z<n*(o>4-(n<2)or z)*(3in(b[j],b[j-1])):
     for k in R[:n]:c=g[e:=j+k];d=b[e];g[e]=[a%4for a in c[:d]+l[k][d+o:]+4*[0]][:6]+c[6:];g[i+~k][6:]=[0]*4
     break
   l=[]
 return[*zip(*g)]