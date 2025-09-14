def p(g):
 u=[[*i,0,0][:15]for i in g]+[[0]*15]*2;G=b'%r#'%u*2;S={G.find(49)}
 for n in range(8484):
  *u,=zip(*u[:15][::1|1-n%3]);*w,=x=b'%r#'%u*2;S={i+n-51for i in S for n in b"06_be"if G[i+n-51]%49<6}
  for i in S:w[i+n%707-min(S)]=G[i]
  if all(i in{49,51,n}for i,n in zip(w,x)):u=eval(bytes(w))
 return[n[:len(i)]for i,n in zip(g,u)]