E=enumerate
p=lambda g:[[r[j]or 1>>(a:=sum(r[:j]+c[:i]))|3>>(b:=sum(r+c)-a)|2*(a==b==sum(r[j:]+c[:i]))for j,[*c]in E(zip(*g))]for i,r in E(g)]