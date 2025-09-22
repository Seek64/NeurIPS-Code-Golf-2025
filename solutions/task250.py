import re
p=lambda g:eval(re.sub("5(([^2]{31}0)*)(?=[^2]*\).*2)",r"0\1+5",f"{*zip(*g[327670:]or p(g*2)),}"))[::-1]