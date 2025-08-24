import re
p=lambda g:[g:=eval(re.sub('(.{55})0, 0, 0'*3,'\%s 1,1,1'*3%(1,2,3),'%9999s'%g))for _ in g][2]