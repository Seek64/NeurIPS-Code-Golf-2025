import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("0((.{31}0, ([^0])){2})",r"\3\1",str(g))));'*20)or g