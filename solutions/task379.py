import re
p=lambda g:[g:=eval(re.sub("0, 8, ([ 0,]+)2|0, (1), .",r"*b''[\2::2],*[2]*len([\1])",f"{*zip(*g[::-1]),}"))for _ in g][7]