import re
p=lambda g:eval(re.sub("0(.{31})2|(?<=5, )0(.{28}2, )0",r"2\1\2 2",str(g[20470:]or p(g*2))))