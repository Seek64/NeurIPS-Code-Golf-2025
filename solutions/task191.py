import re
def p(g):
	L=[0]*25;g=L,*[[0,*r,0]for r in g],L;z=re.sub(*'10',re.sub('[^1]+',lambda x:f"({re.sub('[^%d]'%(4-(']'in x[0])),'.',x[0])})",re.search('1.*1',str(g))[0]))
	for n in[1,-1,1]*4:*g,=zip(*eval('1'.join(re.split(z,str(g[::n])))))
	return[r[1:-1]for r in g[1:-1]]