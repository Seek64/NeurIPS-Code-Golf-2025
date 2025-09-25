import re
p=lambda g:[g:=eval(re.sub(*n.split(),str(g)))for n in[r"0(?=.{34}(\d)) \1",r"0,(?=.{30}5,.0.*([^]05]),) 0,\1|","] ][::-1]"]*12+["5 0"]][-1]