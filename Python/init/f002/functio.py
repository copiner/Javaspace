
def funx1():
    x = 5
    def funy1():
        x *= x
        return x
    return funy1()
#print(funx1())


def funx():
    x = 5
    def funy():
        x *= x
        return x
    return funy
print(funx())
#print(funx()())

def funcx():
    x = [5]
    def funcy():
        x[0] *= x[0]
        return x[0]
    return funcy

print(funcx()())

# nonelocal

def functx():
    x = 5
    def functy():
        nonlocal x
        x *= x
        return x
    return functy
print(functx()())


