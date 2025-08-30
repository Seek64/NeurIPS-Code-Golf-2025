import re
p=lambda g,k=27:-k*g or p(eval(re.sub(*["(\d),?","0(?=(.{%d})*, 0.{%d}0, [^02])"%(n:=3*len(g)+5,n-7),-~len({*g[4]})*"\\1,","2"][k<26::2],str([*zip(*g[::-1])]))),k-1)