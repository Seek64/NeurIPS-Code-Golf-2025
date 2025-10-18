import re
def p(l):
 def p(l):
  return'(%s)'%re.sub('[^%s]'%(4-(')'in l[0])),'.',l[0])
 for e in[1,-1,1]*4:*l,=zip([0]*len(l[0]),*l[::e])
 f=re.sub(*'10',re.sub('[^1]+',p,re.search('1.*1','(%s)'%l)[0]))
 for e in[1,-1,1]*4:*l,=zip(*eval('1'.join(re.split(f,'(%s)'%l[::e]))))
 return[e[3:-3]for e in l[3:-3]]