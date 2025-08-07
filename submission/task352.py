import re
p=lambda g:[g:=eval(re.sub("0(?=(|(...){,2}.{%d})..2)"%(3*len(g[0])-4),"1","%s"%[r[::-1]for r in g[::-1]]))for _ in g][1]