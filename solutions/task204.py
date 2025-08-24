import re
p=lambda g:eval(re.sub(r'(0, |\[)(1[0, ]+)',lambda x:x[1]+x[2].replace('0','27'[len(x[0])%2]),str(g)))