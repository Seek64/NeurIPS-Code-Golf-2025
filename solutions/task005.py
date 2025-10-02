import re
def p(g):
 c=max("987643251",key=str(g).count)
 for n in[11,271,0]*4:s="[^#]"*n;g=eval(re.sub(f'(?=(\d{s})*{c}.*([1-9]){s+c})0',r"\2",f"{*zip(*g[::-1]),}#"*2))
 return g