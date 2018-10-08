
from io import BytesIO
f = BytesIO()
f.write('诗诗'.encode('utf-8'))
print(f.getvalue())

f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
