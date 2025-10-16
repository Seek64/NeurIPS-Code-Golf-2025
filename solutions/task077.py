import re
p=lambda g,k=31:-k*g or p(eval(re.sub("(?<=[24], )[^2](?=.( |.{%d})[24])"%len(3*g),"4",f"{*zip(*g[::-1]),}")),k-1)