
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        'n-1 x --> y'
        hanoi(n-1, x, z, y)
        print(x, '-->', z)#the last one x --> z
        'n-1 y --> z'
        hanoi(n-1, y, x, z)
        

num = int(input('the hanoi tower floor : '))
hanoi(num, 'x', 'y', 'z')
