import re
p=lambda g:exec('g[::-1]=eval(re.sub("0, [^0](?=[^(]*\([^0])","4,4",f"{*zip(*g),}"));'*4)or g