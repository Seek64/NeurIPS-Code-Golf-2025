from re import*
p=lambda g:eval((i:=min(k:=str(g)+'#[]'*X,key=k.count)).join(split(sub(i,f'){(w:=f"[^{i}]")}(',sub(f".(?<={w*S})|(?={w*S}).",".",k)).strip(".()"),k)))