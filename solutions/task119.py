import re
p=lambda g:exec('g[::-1]=zip(*eval(re.sub("0(?=.{40}[38].{40}[238])","3",str(g))));'*40)or g