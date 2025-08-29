import re
p=lambda g:eval(re.sub('([^5]..5)((, 0)+)',lambda x:x[1]+(k:=len(x[2])//3)*f',{5+k}',str(g)))