import re
p=lambda g:exec('s=f"{*zip(*g[::-1]),}";i=s.rfind;d=i("0")-i(j:=min(s,key=i));g[:]=eval(re.sub("(?=(.{%d})+0)\d"%d,j,s,d%8*d%-(len(g)*3+5)));'*4)or g