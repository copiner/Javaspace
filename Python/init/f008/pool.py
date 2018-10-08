#combination
class Turtle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def get_num(self):
        print("trutle : %d, fish : %d" %(self.turtle.num, self.fish.num))

pool = Pool(1, 10)
pool.get_num()

#Mix-in
