import re
p=lambda g:[g:=eval(re.sub("0, [^0](?=[^(]*\([^0])","4,4",f"{*zip(*g[::-1]),}"))for _ in g][3]