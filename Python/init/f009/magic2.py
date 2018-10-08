class A:
    pass

print(type(A))

print(type(len))
print(type(dir))
print(type(int))
print(type(list))


class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    def __sub__(self, other):
        return int.__add__(self, other)

a = New_int(3)
b = New_int(5)

print(a + b)
print(a - b)

class Try_int(int):
    def __add__(self, other):
        return self + other #return a + b  recursion err
    def __sub__(self, other):
        return self - other


class T_int(int):
    def __add__(self, other):
        return int(self) + int(other)
    def __sub__(self, other):
        return int(self) - int(other)

c = T_int(3)
d = T_int(5)
print(c + d)
