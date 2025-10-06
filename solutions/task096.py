import re
def p(l):
 f=re.sub(', ','',str(l+[*zip(*l)]));i=int(max(f,key=f.count));a={0:(0,i)}
 for m in range(10):
  if(m!=i)*re.findall(f'{m}+',f+f[::-1]):n=len(max(re.findall(f'{m}{m}([^]){m}]+){m}|$',f+f[::-1])));a[len(max(re.findall(f'{m}+',f+f[::-1])))*((n>0)+1)+n>>1]=1+n>>1,m
 return[[[a[max(abs(m),abs(e))][1],i][a[max(abs(m),abs(e))][0]>min(abs(m),abs(e))]for m in range(-max(a),max(a)+1)]for e in range(-max(a),max(a)+1)]