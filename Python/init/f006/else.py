
def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d max factor %d' %(num, count))
            break
        count -= 1
    else:
        print('%d is a shushu ' % num)

num = int(input('input a number: '))
showMaxFactor(num)

print(5%1)
print(5//2)
