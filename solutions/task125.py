import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("[38](?=..[46].{40}[46]|.{49}(4|6))",r"4-1%1\1",str(g))));'*20)or g