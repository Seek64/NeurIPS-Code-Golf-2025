import re
p=lambda g:[g:=eval(re.sub('0((.{34}(1)){2})|(((2).{34}){2})0',r'\3\1\4\6',str(g)))for _ in g][9]