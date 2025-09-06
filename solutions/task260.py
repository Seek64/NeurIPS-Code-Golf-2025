import re
S=re.sub
p=lambda g:[g:=eval(S("]","][::-1]",S("0, 0(?=.{28}5, 0)","0,*{*max(g)}-{5,0}",S("0(?=.{34}(\d))",r"\1",S(n,"0",str(g))))))for n in"0"*11+"5"][-1]