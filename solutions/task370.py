import re
p=lambda g:exec('s=f"{*zip(*g[::-1]),}";i=s.rfind;d=i("0")-i(j:=min(s,key=i))-2;g[:]=eval(re.sub("(?=(.,.{%d})+0)."%(d-38*(d==124)),j,s,-(d%-~len(3*g)>25)));'*4)or g