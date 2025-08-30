import re
p=lambda g,h=0:eval(re.sub('0, ([^0]), 0',r'2^\1,78%\1,2^\1',str([*zip(*h or p(g,g))])))