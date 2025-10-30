import re
p=lambda g:eval(g:=re.sub("(?<=4.{34}4)(?=.{34}4(.*0.{31}(4))?)",r"*(X:=g.count)('X\2X')//X('+')+1",str(g)))