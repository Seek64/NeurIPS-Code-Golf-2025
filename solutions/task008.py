import re
r=lambda x:[*map(list,zip(*x[::-1]))]
def p(g,n=3):
	while not re.search(r'2[^\]]+8',str(g:=r(g))):n-=1
	while('2, 8'in g)<1:g=re.sub('(2(, 2)*), 0',r'0,\1',str(g))
	return eval('r('*n+g+')'*n)