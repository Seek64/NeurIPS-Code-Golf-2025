import re
def p(g):
	w=len(g[0])*3-2;l=[str(g)]*3
	for s in['8?5(, )5(.{%d})5(, )5'%w,'2?5(, )5(, )5','2?5'+'(.{%d}...)5'%w*2]*4000:
		G,*l=l;l+=[s[0].join(re.split(s,G,1))]*3
		if('5'in G)<1:return eval(G)