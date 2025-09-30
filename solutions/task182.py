from re import*
p=lambda g,h=0:eval(sub(sub("2|3","1","(.{47})".join(a:=findall(".*5, "+"5.{46}(.{15})"*5,s:=str(h or p(g,g)))[0])),"\%d ".join(a)%(1,2,3,4),s))