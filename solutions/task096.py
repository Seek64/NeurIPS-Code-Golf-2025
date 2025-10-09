import re
def p(a):
 s=re.sub(', ','',str(a+[*zip(*a)]));f=int(max(s,key=s.count));r={0:(0,f)}
 for l in range(10):
  if(l!=f)*re.findall(f'{l}',s):e=len(max(re.findall(f'{l}{l}([^]){l}]+){l}|',s+s[::-1])));r[len(max(re.findall(f'{l}+',s)))*((e>0)+1)+e>>1]=1+e>>1,l
 return[[[r[max(abs(l),abs(s))][1],f][r[max(abs(l),abs(s))][0]>min(abs(l),abs(s))]for l in range(-max(r),max(r)+1)]for s in range(-max(r),max(r)+1)]