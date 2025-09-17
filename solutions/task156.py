import re
def p(g,S=re.subn):g,n=S(x:="(?<=4.{34})4(?=.{34}4)(?!.*0.{31}4)","a",str(g));g,m=S(x[:22],"3^a",g);a=(m<n)+1;return eval(g)