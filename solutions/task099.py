import re
p=lambda g:[g:=eval(re.sub("0(?=(%s.{28})([2-9]))"%s,r"\2",f"{[r[::-1]for r in g[::-1]]}"))for s in["..|..0"]*5+[".{60,66}|"]][5]