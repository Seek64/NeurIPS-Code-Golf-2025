import re
def p(g):
	c=max("987643251",key=str(g).count)
	for n in[11,271,0]*96:s="."*n;x=(re.search(c+s+'([1-9])',g:=str(g))or"00")[1];*g,=zip(*eval(re.sub(f'({c+s}({x+s})*)0',r"\1 "+x,g))[::-1])
	return g