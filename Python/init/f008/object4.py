class C:
    def x(self):
        print('x-man')

c = C()
c.x()
c.x = 1
print(c.x)

#covered
c.x()

