def p(r,l={}):
 for z in range(len(r)-2):
  for e in range(len(r[0])-2):
   i=*[r[z+m//3][e+m%3]==2for m in range(9)],
   if len(o:={r[z+m//3][e+m%3]for m in range(9)})>1>(0 in o):
    o={i:sum(o)-2}
    for m in range(9):r[z+m//3][e+m%3]=0;l[i]=o;i=*[i[2+m%3*3-m//3]for m in range(9)],
 r=[[*m]for m in zip(*r)if sum(m)]
 r=[[*m]for m in zip(*r)if sum(m)]
 for z in range(len(r)-2):
  for e in range(len(r[0])-2):
   i=*[r[z+m//3][e+m%3]==0for m in range(9)],
   if l.get(i,{}).get(i,{}):
    o=l.get(i,{}).popitem()[1]
    for m in range(9):r[z+m//3][e+m%3]=i[m]*2or o
 for z in range(len(r)-2):
  for e in range(len(r[0])-2):
   i=*[r[z+m//3][e+m%3]==0for m in range(9)],
   if l.get(i,{}):
    o=l.get(i,{}).popitem()[1]
    for m in range(9):r[z+m//3][e+m%3]=i[m]*2or o
 return r