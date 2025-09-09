import re
p=lambda g:[g:=eval(re.sub("0(?=([^0)]{15}).*(.)\\1)","\\2",str([*zip(*g)][::-1])))for _ in g][27]