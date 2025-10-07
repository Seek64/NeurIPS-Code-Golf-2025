def p(e):
 for u in range(12):
  r=3-u//4;e=[[*u] for u in zip(*e[::-1])]
  for n in range(len(e)+1-3*r):
   for g in range(len(e[0])+1-3*r):
    u=[e[n+u//(3*r)][g+u%(3*r)] for u in range(3*r*3*r)]
    if u[0]!=u[8]!=3<len({*u}):d=u
 for u in range(12):
  r=3-u//4;e=[[*u] for u in zip(*e[::-1])]
  for n in range(len(e)+1-3*r):
   for g in range(len(e[0])+1-3*r):
    u=[e[n+u//(3*r)][g+u%(3*r)] for u in range(3*r*3*r)]
    if u[:r]==u[r*3*r-3*r:][:r]==d[:1]*r!=u[-r:]==d[8:]*r!=u[~r]==u[r]:
     for u in range(3*r*3*r):e[n+u//(3*r)][g+u%(3*r)]=d[u//(3*r)//r*3+u%(3*r)//r]
 return e