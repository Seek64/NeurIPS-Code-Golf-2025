import re
p=lambda g,R=range(2,9):eval('6'.join(max([re.split((f'(.{{{(len(g[0])-i)*3+4}}}){("(, )0"*i)[4:]}'*j)[7:],str(g),1)for i in R for j in R],key=len)))