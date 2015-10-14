import re
#p=re.compile('aaa{4}')

p=re.compile('\d{10}')
m=p.match('8888888888 email hjghfd@hjhj.com')
print m.group()
print m.span()


