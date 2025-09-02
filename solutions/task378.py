import re
p=lambda g:[g:=eval(re.sub(f"0(?=(.{{%d}}0)*, 0{2*'.{%d}0, ([^0])'})"%(k:=3*len(g)+4,k-6,2*k-2),"\\3",str([*zip(*g[::-1])])))for _ in g][3]