import re
p=lambda g:exec('s=f"{*zip(*g[::-1]),}#";i=s.rfind;d=i("0")-i(j:=min(s,key=i));d-=38*(d==126)+2;g[:]=eval(re.sub("(?=(.,.{%d})+0)."%d,j,s)*(d%(len(g)*3+1)<20)+s);'*4)or g