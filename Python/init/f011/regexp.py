import re
r = re.search(r'calvin', 'calvin company with anna')
print(r)
rr = 'calvin company with anna'.find('calvin')
print(rr)

e = re.search(r'com.','calvin company with anna')
print(e)

t = re.search(r'\.','placekitty.com')
print(t)

n = re.search(r'\d\d','calvin is 18')
print(n)

s = re.search(r'[aeiou]','francis is a boy')
print(s)

st = re.search(r'[a-z]','I love a Girl')
print(st)

stt = re.search(r'[0-9]','I am 20')
print(stt)

c = re.search(r'ab{3}c','abcabbbcc')
print(c)

ce = re.search(r'ab{3,8}c','abcabbbbbcbb')
print(ce)

cha = re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','188')
print(cha)

#ip = re.search()
be = re.search(r'^calvin$', 'calvin')
print(be)

co = re.search(r'(Anna)\1','AnnaAnnaAnna')
print(co)

comb = re.search(r'[.]','placekitty.com')
print(comb)

comt = re.search(r'[a-z]','placekitty.com')
print(comt)

al = re.findall(r'[a-z]','placekitty.com')
print(al)

# * + ?     *? +? ??

html = "<html><title>Anna</title></html>"
h = re.search(r'<.+>', html)
print(h)

ht = re.search(r'<.+?>', html)
print(ht)

w = re.findall(r'\w', '(Anna is tall)')
print(w)

p = re.compile(r'[A-Z]')
print(p.search('Calvin is a Girl'))
print(p.findall("Anna is a Girl"))

