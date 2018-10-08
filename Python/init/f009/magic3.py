class int(int):
    def __add__(self, other):
        return int.__sub__(self, other)

a = int('5')
b = int(3)
print(a + b)

class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)

c = Nint(5)
d = Nint(3)

print(c + d)
print(1 + d) 

class Mint(int):
    def __rsub__(self, other):
        return int.__sub__(other, self)

e = Mint(5)
f = Mint(3)

print(3 - e)


