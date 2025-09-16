import re
p=lambda g:[g:=eval(re.sub(s,r"8^\1",str([*zip(*g[::-1])])))for s in["(?<=[^0], )(0[^)]*[1-9])"]*12+["(8, 0)"]*4][-1]