import re
p=lambda g:eval("".join(re.sub("(?<=4.{34})4(?=.{34}4)","12"[G.count("4")*8>sum(sum(g,[]))],G)for G in re.split(r"(\[[^4]*\])",str(g))))