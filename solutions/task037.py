import re
p=lambda g:g[:~99]or p(eval(re.sub(r"(?<=(.).{34})(?=(.{35})*\1)0",r"\1",str(g[9::-1])))+g)