import re
S=re.sub
def p(g,x=9):b="5, 5, 5";u=b,*[str([5]+[(y!=x)*5for*c,y in zip(*g,r)if x in c]+[5])[1:-1]for r in g if x in r],b;v,y=re.subn(f"(.{{{32-len(u[1])}}})".join(u),S("0","x","\%d ".join(u))%(*range(1,len(u)),),str(g));return-x*g or p((y>0)*eval(S(str(x),"0",v))or g,x-1)