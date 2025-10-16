import re
p=lambda g:g[576:]or p(eval(re.sub("0(?=.{40}[38].{40}[238])","3",f"{*g,*zip(*g[:-13:-1])}")))