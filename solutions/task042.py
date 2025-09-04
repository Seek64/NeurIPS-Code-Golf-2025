import re
p=lambda g,n=15:-n*g or[*zip(*eval(re.sub("(?=.*[^3](, 3){%d}, 0)(?=.{%d}3.{%d}3)0"%(x:=n//4,x*38,x*29-1),"8",str(p(g,n-1))))[::-1])]