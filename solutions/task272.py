import re
p=lambda g,n=7:-n*g or[[[b+3>>1,a>>0**n][a-1]for a,b in zip(r,[0]+r)]for*r,in zip(*p(g,n-1)[::-1])]