class Ball:
    def setName(self, name):
        self.name = name
    def kick(self):
        print('name%s...'% self.name)

a = Ball()
a.setName('A')
b = Ball()
b.setName('B')
a.kick()
b.kick()
