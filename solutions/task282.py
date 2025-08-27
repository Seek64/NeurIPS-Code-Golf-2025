import re
p=lambda g:[g:=eval(re.sub(*s,str([*zip(*g[::-1])])))for s in["54",*6*[("0, 0(?=.{28}4)","5,1")],"40"]][7]