import re
p=lambda g:eval(re.sub('([^5]..5,)([, 0]+)',r'\1*(k:=len([\2]))*[k+5],',str(g)))