#Local Variable   Global Variable

count = 5
def func():
    count = 10
    print(count)

func()
print(count)

coun = 6
def fun():
    global coun
    coun = 10
    print(coun)

fun()
print(coun)

def myfunc():
    print('myfunc()...')
    def yourfunc():
        print('yourfunc()...')
    yourfunc()

myfunc()

#closure
def funcx(x):
    def funcy(y):
        return x*y
    return funcy
x = funcx(8)
print(x)
print(x(5))

print(funcx(6)(7))




