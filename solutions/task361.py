import re
Z=9*[[0]*10]
def p(g):s,e=re.search(r"( [^0]{7}.{24}){3}|(([^0]), \3).{28}\2.{28}",str(g)).span();x=s%32//3;return[g:=[[*map(max,*r)]for r in zip(g,[*Z,*zip(*(Z+g[::-1]+Z)[19-x-e//32:])][9-s//32+x:]+Z)]for _ in g][3]