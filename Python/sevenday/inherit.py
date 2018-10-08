#inherit MixIn
class Runable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')

#1
class Animal(object):
    pass
#2
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#3
class Dog(Mammal,Runable):
    pass
class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runable):
    pass
