e=enumerate
p=lambda g:[[max({*r[i::3]}&{*r[:i]}|{*c[j::3]}&{*c[:j+1]})for i,c in e(zip(*g))]for j,r in e(g)]