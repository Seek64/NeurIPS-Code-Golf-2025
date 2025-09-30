from re import*
p=lambda g:[g:=eval(sub(sub("2|3","1","(.{47})".join(a:=findall(".{46}(.{15})5"*5+".{46}5",s:=str(g))[0])),"\%d ".join(a)%(1,2,3,4),s))for _ in g][3]