def p(r):
 d=[[*b,0,0][:15]for b in r]+[[0]*15]*2;p=b'%r#'%d*2;i={p.find(49)}
 for b in range(8484):
  *d,=zip(*d[:15][::1|1-b%3]);*l,=n=b'%r#'%d*2;i={e+b-51for e in i for b in b"06_be"if p[e+b-51]%49<6}
  for e in i:l[e+b%707-min(i)]=p[e]
  if all(n in{49,51,d}for n,d in zip(l,n)):d=eval(bytes(l))
 return[d[:len(n)]for n,d in zip(r,d)]