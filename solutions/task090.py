import re
p=lambda g:eval('6'.join(max([re.split((f'(..{{{len(g[0])*3-i%8*3}}})0{i%8*"(, )0"}'*(i%5+2))[8:],str(g),1)for i in range(40)],key=len)))