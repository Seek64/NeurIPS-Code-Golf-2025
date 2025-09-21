import re
p=lambda g:eval([g:=re.sub('0(?=(.{34}%s){2})'%x,x,str(g)[::-1])for x in"21"*8][-1])