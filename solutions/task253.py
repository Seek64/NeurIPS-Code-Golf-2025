F=0,1,2,3
p=lambda g:[[max(min(g[p//12+v//2][p%12+v%2]for v in F if x*y%3|v^y&6^x//2^3)for p in range(144))for x in F]for y in F]