import re
p=lambda g:[g:=eval(re.sub(f'{n}([^(]*)0(?=, {8%n})',r'0\1n',f"{*zip(*g[::-1]),}"))for n in(7,3,3)*8][-1]