def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print('32cel = %.2ffah' % c2f(32))
    print('99fah = %.2fcel' % f2c(99))

test()

