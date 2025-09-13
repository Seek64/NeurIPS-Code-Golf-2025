import re
p=lambda g,n=23:-n*g or[*zip(*eval(re.sub("(?=0.*0(, 3){%d}, 0)(?=.{%d}3)"*2%(x:=n%5,x*38,x,x*67),"8|",str(p(g,n-1))))[::-1])]