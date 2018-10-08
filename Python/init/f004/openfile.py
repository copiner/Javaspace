
f = open("app.txt")
print(f)
#print(f.read())
#print(f.read(5))
#print(f.tell())

print(f.seek(6, 0))
print(f.readline())

print(list(f))

f.seek(0, 0)
for line in f:
    print(line)

f.close()

p = open("test.txt", 'w')
p.write('calvin is girl')
p.close()
