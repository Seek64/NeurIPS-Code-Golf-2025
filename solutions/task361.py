import re
Z=[[0]*10]
def p(g):s,e=re.search(r"( [^0]{7}.{24}){3}|([^0]), \2.{28}\2, \2.{28}",str(g)).span();d=s//32-s%32//3;a=s%32//3-10+e//32;return[g:=[[*map(max,*r)]for r in zip(g,d*Z+[*zip(*a*Z+g[::-1][max(0,-a):]+9*Z),*9*Z][max(0,-d):])][:10]for _ in g][3]