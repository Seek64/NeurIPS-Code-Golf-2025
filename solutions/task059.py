def p(g):
	*G,=b'%r'%g
	for i,s in zip(L:=b"\0#&)FIL",S:=[sum(G[k+i*4+2]for k in L)for i in L]):
		for k in L:G[k+i*4+2]=sorted({*G}-{53})[2+s//max(S)]
	return eval(bytes(G))