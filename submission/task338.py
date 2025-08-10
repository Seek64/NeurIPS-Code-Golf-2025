import re
p=lambda g:[g:=eval(re.sub(*s,f"{g}"))for s in[("0(?=..[23].{%d}[23])"%(3*len(g[0])-2),"3")]*30+["20"]][-1]