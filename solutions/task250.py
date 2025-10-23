import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("5(([^2]{31}0)*)(?=[^2]*\).*2)",r"0\1+5",str(g))));'*20)or g