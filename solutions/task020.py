import re
p=lambda g:[g:=eval(re.sub("0(?=.{%d}(.))(?=.{%d}[^0][^1-9]*$)"%(57|324%x,x),r"\1",f"{*zip(*g[::-1]),}"))for x in b"b?"*12][-1]