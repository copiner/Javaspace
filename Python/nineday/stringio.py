
from io import StringIO
f = StringIO()
f.write('francis')
print(f.getvalue())

f = StringIO('francisgoodnight')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

