class Parent:
    def sayHi(self):
        print('hi...')
    def sayNo(self):
        print('no...')
class Child(Parent):
    def sayHi(self):
        print('c_hi...')

c = Child()
c.sayHi()
c.sayNo()
