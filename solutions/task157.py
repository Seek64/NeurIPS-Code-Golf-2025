def p(g):
 g=[*map(list,zip(*g))]
 for i in range(64):
  w=4-i//16;i%=16-w;m=max((-(1in sum(g[j:j+w],l:=g[i:i+w])),-len(q:={y.index(max(y))-x.index(min(x))for x,y in zip(g[j:],l)}),min(q),j%w,j)for j in range(16-w))
  for j in range(w*4*all(5in r for r in l)):g[m[4]+j//4][6-m[2]+j%4]+=l[j//4][6+j%4]%4;g[i+j//4][6+j%4]=0
 return[*map(list,zip(*g))]