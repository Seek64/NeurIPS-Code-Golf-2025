import re
p=lambda g:eval([g:=re.sub(r"0(?=([^]0]{15}).*(.)\1)",r"\2",str(g)[::-1])for _ in g][-2])