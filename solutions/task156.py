import re
def p(g,S=re.subn):g,n=S("(?<=4.{34})4(?=.{34}4)","a",str(g));g,m=S("(?=a.*0.{31}4)","3^",g);a=2-m*2//n;return eval(g)