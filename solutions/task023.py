import re
def p(g):
	w=len(g[0])*3-2;l=[f'{g}#28']*3
	for s in['8?5(, )5(.{%d})5(, )5'%w,'2?5'+'(, )5'*2,'2?5'+'(.{%d}...)5'%w*2]*1300:G,*l=l;l+=[s[0].join(re.split(s,G,1))]*3
	return eval(min(l,key=set))