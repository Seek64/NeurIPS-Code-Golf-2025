import re
def p(e):
 def p(e):
  return'(%s)'%re.sub('[^%d]'%(4-(')'in e[0])),'.',e[0])
 for r in[1,-1,1]*4:*e,=zip([0]*len(e[0]),*e[::r])
 z=re.sub(*'10',re.sub('[^1]+',p,re.search('1.*1','(%s)'%e)[0]))
 for r in[1,-1,1]*4:*e,=zip(*eval('1'.join(re.split(z,'(%s)'%e[::r]))))
 return[r[3:-3]for r in e[3:-3]]