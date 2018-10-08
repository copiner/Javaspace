import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('position : ', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self): 
        Fish.__init__(self) #Fish.__init__(shark)
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('eating...')
            self.hungry = False
        else:
            print('enough')

shark = Shark()
shark.move()
