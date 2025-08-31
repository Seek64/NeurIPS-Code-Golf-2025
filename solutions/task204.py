import re
p=lambda g:eval(re.sub('([^1]..1,)([^1]+)',r'\1*(k:=len([\2]))*[2+k%2*5],',str(g)))