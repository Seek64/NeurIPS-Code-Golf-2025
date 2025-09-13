import re
def p(g):
 l=sum(g,[]);a,b,c,*d={}.fromkeys((9*l[1:])[7::30]+l[240:])
 for i in[i for i in range(838)if(l[i+62]==c)and({*l[i+61:i+64]}&{a,b}or(j:=i))]+[j]:
  for o in range(25):g[i//30+o//5][i%30+o%5]=a*(i==j)or(l[o//5*30+o%5+i],l[o//5*30+o%5+j])[l[o//5*30+o%5+j]!=a!=b==l[o//5*30+o%5+i]]
 return[g:=eval(re.sub(f"{b}, (?=([^{a}], )\\1+{c})","\\1",str([*zip(*g[::-1])])))for i in l][63]