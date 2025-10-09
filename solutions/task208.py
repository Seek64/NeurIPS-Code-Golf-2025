from re import*
p=lambda g:eval((i:=min(k:=str(g)+'#[]'*X,key=k.count)).join(split(sub(i,w:=f'[^{i}]',sub(f'({w}+)',r'(\1)',sub(w*30+'+',lambda x:'.'*len(x[0]),*findall(i+'.*'+i,k)))),k)))