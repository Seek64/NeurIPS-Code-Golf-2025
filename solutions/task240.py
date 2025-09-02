R=range(19)
p=lambda g:[g:=[[g[y][x]|g[y][[~x,y+2][18-y>x%2*x>y]]for y in R]for x in R]for _ in R][5]