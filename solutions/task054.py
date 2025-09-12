import re
def p(g):
 l=sum(g,[]);a,b,*d={}.fromkeys(g[8]+l);c=min(d,key=lambda x:l[::-1].index(x)+l.index(x))
 for i in[*{i for i in range(900)if(l[i]==c)and((l[i+1]==b)or(~-(a in l[i-1:i+2])and(j:=i)))}-{j},j]:
  for o in range(25):k=o//5*30+o%5-62;l[i+k]=a*(i==j)or(l[i+k],l[j+k])[l[j+k]!=a!=b==l[i+k]]
 g=[[l.pop(0)for i in range(30)]for i in range(30)]
 return[g:=eval(re.sub(r"%d(?=, ([^%d])(, \1)+, %d)"%(b,a,c),"\\1",str([*zip(*g[::-1])])))for i in 2*g][-1]