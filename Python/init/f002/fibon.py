#fenzhishixiang

def fib(n):
    if n < 1:
        print('error')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = int(input('input a int : '))
result = fib(num)
print('%d month later total is : %d' %(num, result))
