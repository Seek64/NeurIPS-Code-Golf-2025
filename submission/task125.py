import re
S=re.sub
p=lambda g:[g:=eval(S("[38](?=..[46].{40}[46])","4",S("8(?=.{49}6)","3","%s"%[*map(list,zip(*g[::-1]))])))for _ in 2*g][15]