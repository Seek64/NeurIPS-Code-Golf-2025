E=enumerate
p=lambda g:[[r[j]or(a:=sum(r[:j]+c[:i]))<1or(3>>(b:=sum(r+c)-a))+2*(a==b==sum(r[j:]+c[:i]))for j,[*c]in E(zip(*g))]for i,r in E(g)]