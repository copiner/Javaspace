class Base:
    def pull(self):
        print('Base...')

class Ball:
    def push(self):
        print('Ball...')

class buik(Base, Ball):
    pass

b = buik()
b.pull()
b.push()

