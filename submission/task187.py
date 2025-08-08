import re
S=re.sub
p=lambda g:[g:=eval(S("2(?=..[\D3])","3",S(*"02",f"{[*map(list,zip(*g[::-1]))]}")))for _ in g*4][-1]