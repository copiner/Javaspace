
def fib(num):
    n,a,b = 0,0,1
    while n < num:
        print(b)
        a, b = b, a + b
        n=n+1
    return 'done'

fib(6)

def fibo(num):
    n,a,b = 0,0,1
    while n < num:
        yield b
        a, b = b, a + b
        n=n+1
    return 'done'

f = fibo(6)
print(f)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3 
    print('step 3')
    yield 5

o = odd()
print(next(o))
print(next(o))
print(next(o))
