import re;r=re.sub
def p(g):S=r("[^1-79]",X:="(.)",G:=str(g)).strip(X);h=r(D:="[1-79]","0",G);[h:=r(r(D,"8",S),r(r"\(..",r"\\g<%d>",S)%(*range(1,S.count(X)+1),),h)for _ in g];return eval(h)