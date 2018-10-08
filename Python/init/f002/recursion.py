
def factrial(n):
    result = n
    for i in range(1, n):
        result *=i
    return result

num = int(input("input a int : "))
result = factrial(num)
print('%d factrial : %d' %(num, result))

#recursion
def factri(n):
    if n == 1:
        return 1
    else:
        return n * factrial(n-1)

number = int(input("input a integer : "))
result = factri(number)
print('%d factrial : %d' %(number, result))


