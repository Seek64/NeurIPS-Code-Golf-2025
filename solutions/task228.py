import re
p=lambda g,n=-3:n*g or p([*zip(*eval(re.sub(r"0(.{34}([1-9]).*)(?!\2|0)(\d)(, \2.{31}\2)",r"\3\1 0\4",str(g),1))[::-1])],n+1)