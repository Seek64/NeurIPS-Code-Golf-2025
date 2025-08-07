import re
S=re.sub
p=lambda g:[g:=eval(S("0(?=(|.{6}).{25}2)","4",S("0(?=(|.{26})..1)","7","%s"%[r[::-1]for r in g[::-1]])))for _ in g][1]