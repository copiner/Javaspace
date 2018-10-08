
def calc_sum(*args):
    ax=0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1,2,3))

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f1 = lazy_sum(1,3,5,7,9)
print(f1)
print(f1())
f2 = lazy_sum(1,3,5,7,9)
print(f1 == f2)
print(f2())
