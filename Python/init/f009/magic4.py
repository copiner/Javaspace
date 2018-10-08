class A():
    def __str__(self):
        return 'Anna'

a = A()
print(a)

class B():
    def __repr__(self):
        return 'Calvin'
b = B()
print(b)

import time as t
class MiTimer():
    def start(self):
        self.start = t.localtime()
        print("start...")
    def stop(self):
        self.stop = t.localtime()
        self._calc()
        print("end...")
    def _calc(self):
        self.lasted = []
        self.prompt = 'total : '
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt += str(self.lasted[index])
        print(self.prompt)

#t1 = MiTimer()
#t1.start()
#t1.stop()
