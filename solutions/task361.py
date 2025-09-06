import re
Z=9*[[0]*10]
def p(g):s,e=re.search(r"( [^0]{7}.{24}){3}|([^0]), \2.{28}\2, \2.{28}",str(g)).span();d=s//32-s%32//3;a=s%32//3-10+e//32;return[g:=[[*map(max,*r)]for r in zip(g,[*Z,*zip(*(Z+g[::-1]+Z)[9-a:]),*Z][9-d:])][:10]for _ in g][3]