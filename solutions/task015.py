import re
p=lambda g:[g:=[*zip(*eval(re.sub('0(.{31}2|..(1))',r'4\2%17\1',str(g[::-1]))))]for _ in g][7]