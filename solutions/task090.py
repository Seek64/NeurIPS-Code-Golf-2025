import re
p=lambda g:eval('6'.join(max([re.split((f'(.{{{len(g[0])*3-i%7*3-2}}}){("(, )0"*(i%7+2))[4:]}'*(i%5+2))[7:],str(g),1)for i in range(35)],key=len)))