import re
p=lambda g,n=7:-n*g or p(eval(re.sub("0(?=(, 0, .{%d})*(?<=0, [^02]))"%len(3*g),"02"[n<4],str([r for*r,in zip(*g[::-1])for _ in{*n//6*g[-1],0}]))),n-1)