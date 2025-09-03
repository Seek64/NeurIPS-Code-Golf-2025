import re
p=lambda g:[g:=eval(re.sub('0(?=(.{%d}5){2})'%(len(g)*3+4),k,str([*zip(*g[::-1])])))for k in'3421'*2][7]