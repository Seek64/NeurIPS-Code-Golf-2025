import re
p=lambda g:[g:=eval(re.sub("5(.{%d})0(?=(.{%d}0)*.{%d}2)"%(n,n,n),"0\\1 5",str([*zip(*g[::-1])])))for n in b'""'*20][-1]