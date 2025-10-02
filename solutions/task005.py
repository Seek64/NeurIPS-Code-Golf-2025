import re
def p(g):
 c=max("987643251",key=str(g).count)
 for n in[11,247,259,271,0]*2:s="[^#]"*n;g=re.sub(f'(?=.*([1-9]){s+c})(?=(\d{s})*{c})0',r"\1","%s#"%g*2)[1364::-1]
 return eval(g)