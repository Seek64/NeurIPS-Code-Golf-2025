import re
p=lambda g:[g:=eval(re.sub(*s,str([*zip(*g[::-1])])))for s in[(r"\((.), 0([^)]*)\1",r"(\1,\1\2 0")]*7+[("(\d)",r"\1*(sum(g,()).count(\1)>3)")]][7]