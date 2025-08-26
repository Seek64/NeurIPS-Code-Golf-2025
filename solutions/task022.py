r=-1,0,1
p=lambda g:[[dict(sorted(zip(o:=sum(g,[]),o[x*11+y:]+o)))[5]for y in r]for x in r]