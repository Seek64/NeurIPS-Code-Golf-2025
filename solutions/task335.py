def p(g):
 (i,j),(x,y)=map(divmod,map(sum(g,[]).index,[2,8]),2*[len(g[0])])
 while j-y:x+=(x<i)-(i<x);g[x][y]=4;y+=(-1,1)[y<j]*(x==i)
 return g