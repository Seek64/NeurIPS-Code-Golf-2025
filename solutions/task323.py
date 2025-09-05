import re
S=re.sub
p=lambda g,n=0:eval(S("]","][::-1]",S("0(?=(.{76})*(.{40}|(...){25,27})8)","5",str(n or p(g,g)))))