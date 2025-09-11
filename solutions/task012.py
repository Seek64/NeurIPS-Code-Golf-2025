import re
p=lambda g:eval([g:=re.sub(r"0(?=.{%d}([^0])..(.)..\1)"%x,f"\{895%x%5}",str(g)[::-1])for x in b'HHNB%'*2][-1])