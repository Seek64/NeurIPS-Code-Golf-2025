import re
p=lambda g:eval(re.sub("|1(?=.{%d}([2-9]))(?<=[2-9].{%d})"*2%(8,9,77,78),r"\1\2",str(g)))