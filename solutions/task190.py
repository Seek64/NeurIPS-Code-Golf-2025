import re
p=lambda g:g[200:]or p(eval(re.sub("0((.{31}0, ([^0])){2})",r"\3\1",f"{*g,*zip(*g[:-11:-1])}")))