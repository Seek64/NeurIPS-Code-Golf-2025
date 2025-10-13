import re
p=lambda g,n=-35:n*g or eval(re.sub("([^02]), 2(.{28})0",r"*[\1]*3\2\1,2",f"{*zip(*p(g,n+1)),*g}"))[8::-1]