
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

#pass
def noop():
    pass

#import
import math
def quadratic(a, b, c):
    sum = a + b + c
    mul = a*b*c
    return sum, mul

q=quadratic(1,2,3)
print(q)
