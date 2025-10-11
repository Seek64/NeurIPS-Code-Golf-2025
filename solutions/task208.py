from re import*
p=lambda g:eval((i:=min(k:=str(g)+'#[]'*X,key=k.count)).join(split(sub(i,f')[^{i}](',sub("[^%s]+"%i*18,lambda x:'.'*len(x[0]),k)).strip(".()"),k)))