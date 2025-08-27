import re
p=lambda g:[g:=eval(re.sub(*s,str([*zip(*g[::-1])])))for s in[("(?<=[^0], )0(?=[^)]*[1-9])","8")]*12+[("8, 0","0,0")]*4][-1]