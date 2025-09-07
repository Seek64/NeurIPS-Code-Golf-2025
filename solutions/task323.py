import re
p=lambda g:eval([g:=re.sub("0(?=(.{76})*(.{40}|(...){25,27})8)","5",str(g))[::-1]for _ in g][1])