from re import*
p=lambda g:eval((i:=min(k:=str(g)+'#[]'*X,key=k.count)).join(split(sub(i,w:=f'[^{i}]',sub(f'({w}+)',r'(\1)',sub(f".(?<={w*S})|(?={w*S}).",".",k).strip("."))),k)))