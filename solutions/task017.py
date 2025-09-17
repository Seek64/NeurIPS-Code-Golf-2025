import re
p=lambda g:[g:=eval(re.sub("0(?=([^0)]{12}).*(.)\\1)","\\2",f"{*zip(*g[::-1]),}"))for _ in g][19]