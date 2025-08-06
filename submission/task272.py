import re
p=lambda g:eval(re.sub("(?<=[^2].{%s}[^2]..)2(?!..(|..{%s})2)"%(w:=3*len(g[0])-2,w),"1",99*" "+"%s"%g))