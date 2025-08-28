def p(g):
	w=bytearray(b'%r'%g);q=[i for i in range(320)if 4!=w[i]%49<9]
	while~(o:=w.find(53)):
		for i in q:w[o+i-q[0]]=w[i]
	return eval(w)