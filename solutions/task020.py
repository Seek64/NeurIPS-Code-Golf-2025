def p(g):
 for _ in 2*g:E=enumerate;x,y=[(i,j)for i,r in E(g)for j,c in E(zip(*g))if{*r}&{*c}-{0}][0];g[x+4][y]|=g[x][y];g[x+2][y]|=g[x][y+2];g[x+1][y+1]|=g[x+1][y+3];g=[r[::-1]for*r,in zip(*g)]
 return g