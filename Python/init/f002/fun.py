
def func():
    print("first func")
    print("nice")

func()

def secfunc(name):
    print(name + " is girl")

secfunc("calvin")

def add(num1, num2):
    return num1 + num2

print(add(2, 5))

def funcfile(tip):
    'tip is parameter'
    print(tip + ' pass into funcfile is argument')

funcfile("gay")
print(funcfile.__doc__)


def saysome(name, words):
    print(name + ' --> '+ words)

saysome('francis', 'is boy')
saysome(words = 'is boy', name = 'francis')

def say(name='calvin', words='known less'):
    print(name + ' --> ' + words)

say()
say('xiao')
say('xiao', 'is a girl')


def unknown(*params):
    print('argument : ', len(params))
    print('the second argument : ', params[1])

unknown(9,8,7,6,5,4,3)

def unknow(*params, exp='hi'):
    print('argument : ', len(params), exp)
    print('the second argument : ', params[1])

unknow(9,1,7,2,5,4,3)
unknow(9,8,2,7,5,4,3, exp='yoyo')




