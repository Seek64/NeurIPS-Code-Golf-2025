def p(f):
 for i in range(4):
  d=sum(f,[]);b,h,g,*e={d.index(i):0for i in d}
  for i in range(g-h>>2):d[g+~i*2]=d[h-~i*2]=5
  f=[d[i-len(f[0])::-len(f[0])]for i in range(len(f[0]))]
 for i in range(4):
  d=sum(f,[]);b,h,g,*e={d.index(i):0for i in d}
  for i in range(8):d[g-i%-3+~(i//3%-3)*len(f[0])-3]=d[e[0]]
  f=[d[i-len(f[0])::-len(f[0])]for i in range(len(f[0]))]
 return f