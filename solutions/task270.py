import re
p=lambda g,n=7:g*-n or p(eval(re.sub(f'({1+n//4}),([^(]*)({7>>n//4})',r'\1,\3+\2 0',f"{*zip(*g[::-1]),}")),n-1)