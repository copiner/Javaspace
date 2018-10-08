
def calc(numbers):
    sum=0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc([1,2,3]))
print(calc((1,2,3,4)))

def cal(*numbers):
    sum=0
    for n in numbers:
        sum = sum + n*n
    return sum

print(cal(1,2,3,4))
print(cal(1,2,3,4,5))

nums = [2,3,4]
print(cal(nums[0],nums[1],nums[2]))

print(*nums)
print(cal(*nums))

