import re
S=re.sub
p=lambda g,n=0:eval(S("]","][::-1]",S("0(?=(.{76})*(.{40}|.{75}(.{3}){,2})8)","5",str(n or p(g,g)))))