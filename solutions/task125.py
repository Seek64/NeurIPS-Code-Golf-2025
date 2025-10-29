import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("[38](?=(..(4|6).{40}|.{49})[46])",r"4-1\2%2",str(g))));'*20)or g