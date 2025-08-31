import re
p=lambda g:[g:=eval(re.sub("([^2]), 2, 0(.{25})0, 0"[:n+4],r"\1,\1,\1\2\1,2"[:n],str([*zip(*g[::-1])])))for n in[19]*32+[8]*4+[5]*4][-1]