#import temperature

#print('32cel = %.2ffah' % temperature.c2f(32))
#print('99fah = %.2fcel' % temperature.f2c(99))

#from temperature import *
#from temperature import c2f, f2c

#print('32cel = %.2ffah' % c2f(32))
#print('99fah = %.2fcel' % f2c(99))


import temperature as tc

print('32cel = %.2ffah' % tc.c2f(32))
print('99fah = %.2fcel' % tc.f2c(99))


