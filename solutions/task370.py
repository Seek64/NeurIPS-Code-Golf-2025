import re
p=lambda g:exec('s=f"{*zip(*g[::-1]),}";j=max(map(i:=s.find,{*s[:-2]}));d=j-i("0")-2;d-=38*(d==124);g[:]=eval(re.sub(f"(?<=(0|{s[j]})..{{{d*(d>d%(len(g)*3+1)<20)}}})\d",s[j],s));'*16)or g