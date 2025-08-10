E=enumerate
p=lambda g:[[sum({*c[:i+1]}&{*c[i:]})or sum({*r[:j+1]}&{*r[j:]})for j,c in E(zip(*g))]for i,r in E(g)]