import re
p=lambda g:[g:=eval(re.sub(s[1:],s[0],f"{[*map(list,zip(*g[::-1]))]}"))for s in["10"]*4+["01(?=..[\D0])"]*32][-1]