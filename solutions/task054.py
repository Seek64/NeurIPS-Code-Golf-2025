import re
def p(g):
 l=sum(g,[]);a,b,c,*d=sorted({*l},key=lambda x:l[::-1].index(x)+l.index(x)-l.count(x))
 for i in[i-62for i in range(900)if(l[i]==c)and({*l[i-1:i+2]}&{a,b}or(j:=i-62))]+[j]:
  for o in range(25):g[i//30+o//5][i%30+o%5]=a*(i==j)or(l[i+o//5*30+o%5],l[j+o//5*30+o%5])[l[j+o//5*30+o%5]!=a!=b==l[i+o//5*30+o%5]]
 return[g:=eval(re.sub(f"{b}, (?=([^{a}], )\\1+{c})","\\1",str([*zip(*g[::-1])])))for i in 2*g][-1]