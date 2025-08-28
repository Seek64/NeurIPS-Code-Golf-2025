import re
p=lambda g:eval(re.sub(r'((?<=([^1]).{8})|(?<=(.).{77}))1(?=.{8}\2|.{77}\3)',r'\2\3',str(g)))