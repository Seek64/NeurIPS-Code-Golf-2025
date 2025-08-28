def p(g):
	w=len(g);k=2-w%2;g=[[3]*k]*k
	for _ in'@'*(~1&~-w):g=[[3,i,*r]for*r,i in zip(*g,[3]+[0]*w)][::-1]
	return[*zip(*g)]