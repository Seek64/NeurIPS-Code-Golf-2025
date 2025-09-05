import re
def p(g):l=len(g[0])*3-2;return max([p(x)for i in["8?5(, )5(.{%d})5(, )5"%l,"2?5"+"(.{%d}...)5"%l*2,"2?5(, )5(, )5"]if(x:=eval(i[0].join(re.split(i,s:=str(g),1))))!=g]+[0**('5'in s)*g])