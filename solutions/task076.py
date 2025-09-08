def p(g):
	u=[[*r,0,0][:15]for r in g]+[[0]*15]*2;G=b'%r'%u*2;S={G.index(49)}
	for n in range(8484):
		*u,=zip(*u[:15][::1|1-n%3]);S|={i+j-51for i in S for j in b"06_be"if G[i+j-51]%49<6};*w,=x=b'%r#'%u*2
		for i in S:w[i+n%707-min(S)]=G[i]
		if all(k in{49,51,l}for k,l in zip(w,x)):u=eval(bytes(w))
	return[r[:len(g[0])]for r in u][:len(g)]