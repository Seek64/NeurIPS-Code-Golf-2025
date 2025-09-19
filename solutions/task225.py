import re
p=lambda g:[g:=eval(re.sub(r"0(?=.{27}(...)?(.{20})?0, ([^0])(?!, \3).{19}0)",r"\3",f"{*zip(*g[::-1]),}"))for _ in g][3]