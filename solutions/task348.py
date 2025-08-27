import re
p=lambda g:[g:=eval(re.sub("0(?=.{%d}(.{6})?(7|8))"%(3*len(r)-2),r"15^\2",str(g)))for r in 2*g][9]