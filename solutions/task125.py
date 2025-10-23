import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("[38](?=..[46].{40}[46])|(8)(?=.{49}6)",r"4\1%5",str(g))));'*20)or g