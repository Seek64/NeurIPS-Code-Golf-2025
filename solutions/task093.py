import re
p=lambda g:[g:=eval(re.sub('5([^)]*), [^50]',r'5,5\1',str([*zip(*g[::-1])])))for _ in g][11]