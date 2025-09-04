import re
S=re.sub
p=lambda g,n=15:-n*g or p([r[::-1]for r in eval(S("0, 0(?=.{28}5, 0)","0,*{*max(g)}-{5,0}",S("0(?=.{34}(\d))",r"\1",S("05"[n<9],"0",str(g)))))[::-1]],n-1)