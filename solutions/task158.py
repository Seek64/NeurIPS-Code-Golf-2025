def p(n):
 for h in range(12):
  d=3-h//4;n=[[*h]for h in zip(*n[::-1])]
  for e in range(len(n)+1-3*d):
   for g in range(len(n[0])+1-3*d):
    i=[n[e+h//(3*d)][g+h%(3*d)]for h in range(3*d*3*d)]
    if i[0]!=i[8]!=3<len({*i}):p=i
 for h in range(12):
  d=3-h//4;n=[[*h]for h in zip(*n[::-1])]
  for e in range(len(n)+1-3*d):
   for g in range(len(n[0])+1-3*d):
    i=[n[e+h//(3*d)][g+h%(3*d)]for h in range(3*d*3*d)]
    if i[:d]==i[d*3*d-3*d:][:d]==p[:1]*d!=i[-d:]==p[8:]*d!=i[~d]==i[d]:
     for h in range(3*d*3*d):n[e+h//(3*d)][g+h%(3*d)]=p[h//(3*d)//d*3+h%(3*d)//d]
 return n