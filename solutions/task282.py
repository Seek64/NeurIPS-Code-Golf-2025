import re
p=lambda g:[g:=eval(re.sub('0, ([^0]), 0',r'2^\1,78%\1,2^\1',str([*zip(*g)])))for _ in g][1]