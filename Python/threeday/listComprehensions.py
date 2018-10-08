
L = list(range(1,11))
print(L)
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

L=[x*x for x in range(1, 11)]
print(L)

L=[m+n for m in 'ABC' for n in 'XYZ']
print(L)

d={'X':'A', 'Y':'B', 'Z':'C'}
for k, v in d.items():
    print(k, '=', v)

L=[k+' = '+v for k, v in d.items()]
print(L)

UPPER=['DUNCAN', 'PARKER', 'MANU', 'BOBO']
low = [s.lower() for s in UPPER]
print(low)
