import re
p=lambda g:eval(re.sub(r"1(?=(.{8}|.{77})([2-9]))((?<=\2.{78})|(?<=\2.{9}))",r"\2",str(g)))