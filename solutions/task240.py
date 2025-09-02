R=range(19)
p=lambda g,k=-7:k*g or p([[g[y][x]|g[y][[~x,y+2][18-y>x%2*x>y]]for y in R]for x in R],k+1)