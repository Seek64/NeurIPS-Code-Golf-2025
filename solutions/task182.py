from re import*
p=lambda g:[g:=eval(sub("(.{47})%s"*5%eval(sub("2|3","1",str(a:=findall(".{46}(.{15})5"*5+".{46}5",s:=str(g))[0]))),"\%d %%s"*5%(1,2,3,4,5)%a,s))for _ in g][3]