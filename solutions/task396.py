import re
def p(g,S=str):*_,a,b=sorted('123456789',key=S(g).count);exec("g[:]=zip(*g[(max(re.findall(b+f'(?:, {b})+',S(g)))in S(g[-1]))-2::-1]);"*96);return eval(re.sub(b,a,S(g)))