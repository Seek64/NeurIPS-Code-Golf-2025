def p(i,*s):
 e,*g=len(i[0]),
 for f in range(len(i)*e):
  for q,h,p in (n:=[(t:=i[f//e][f%e],f//e,f%e)]*t):i[h][p]=0;n+=[(((i+i)[h+f//3-1]+[0])[p+f%3-1],h+f//3-1,p+f%3-1)for f in range(9)if((i+i)[h+f//3-1]+[0])[p+f%3-1]]
  g+=n*(len(n)<5*t);s+=*zip(*[((q,p-f%e,h-f//e),(q,f//e-h,p-f%e))for q,h,p in n]),
 for f in range(len(i)*e):
  for n in sum([(*zip(*[((q,p,h),(q,-h,p))for q,h,p in n]),)for n in s],s):
   for q,h,p in (n:=[(q,h+f//e,p+f%e)for q,h,p in n])*(len({*g}&{*n})>2):i[h][p]=q
 return i