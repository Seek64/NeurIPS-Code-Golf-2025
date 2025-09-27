import re
def p(e):
 def p(e):
  return'(%s)'%re.sub('[^%a]'%(4-(')'in e[0])),'.',e[0])
 for a in[1,-1,1]*4:*e,=zip([0]*len(e[0]),*e[::a])
 f=re.sub(*'10',re.sub('[^1]+',p,re.search('1.*1','(%s)'%e)[0]))
 for a in[1,-1,1]*4:*e,=zip(*eval('1'.join(re.split(f,'(%s)'%e[::a]))))
 return[a[3:-3]for a in e[3:-3]]