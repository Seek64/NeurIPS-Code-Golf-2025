import re
def p(g):c=max("987643251",key=str(g).count);return[g:=eval(re.sub(f'(?=(\d{"."*n})*{c}.*([^0]){"."*n+c})0',r"\2",f"{*zip(*g[::-1]),}#"*2))for n in[11,271,0]*4][-1]