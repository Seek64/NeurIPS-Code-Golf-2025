import re
p=lambda g:eval(re.sub('([^1]..1)((, 0)+)',lambda x:x[1]+(k:=len(x[2])//3)*f',{2+k%2*5}',str(g)))