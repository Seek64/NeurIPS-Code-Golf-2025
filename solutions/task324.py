def p(m):
 s=sum(m,t:=[]);r=sorted(s,key=s.count)[:2]
 for d in range(len(m)):
  for o in range(len(m[d])):
   if m[d][o]in r:s[m[d][o]]=s[max(s,key=[m[d][o-1],m[d][o-len(m[d])+1],m[d<1][o]].count)]=m[d][o];r+=-d-o,;t+=d-o,
 for d in range(len(m)):
  for o in range(len(m[d])):
   if d-o in t or-d-o in r:m[d][o]=s[m[d][o]]
 return m