import re
p=lambda g:eval(re.sub("(?<=5.{28}5..)5(?=..5.{28}5)","2","%s"%g))