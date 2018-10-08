#golden section 0.618

#iterable
def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("error")
        return -1

    while (n-2)>0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    
    return n3

num = int(input("input a integer : "))
result = fib(num)
print('%d num month later total %d' %(num, result))
