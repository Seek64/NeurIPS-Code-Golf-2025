import re
def p(g):
	a,b,_=sorted(set(w:=sum(g,[])),key=w.count)
	for _ in g*4:*g,=zip(*g[(max(re.findall(f'{b}(?:, {b})+','%s'%g))in str(g[-1]))-2::-1])
	return[[a*(c>0)for c in r]for r in g]