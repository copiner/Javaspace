
#format()
form = "{0} love {1}.{2}".format("cal","frn","dun")
print(form)

forma = "{a} love {b}.{c}".format(a = "cal",b = "frn",c = "dun")
print(forma)

fo = "{0} love {b}.{c}".format("pl",b = "frn",c = "dun")
print(fo)

#error
#formate = "{a} love {b}.{0}".format(a = "pl",b = "frn","dun")

print("{{0}}".format("no print"))
print("{0:.1f}{1}".format(12.654,'GB'))

print('%c' % 97)
print('%c %c %c' %(97, 98, 99))
print('%s' % 'love is love')
print('%d + %d = %d' % (4, 5, 4+5))

print('%5.1f' %27.618)

print('%#o' %10)
print('%#X' %108)
