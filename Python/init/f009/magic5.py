import time as t
class MiTimer():
    def __init__(self):
        self.unit = ['Y', 'M', 'D', 'h', 'm', 's']
        self.prompt = "not begin..."
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        self.prompt = "first obj.start() than obj.stop() last obj"
        print("start...")
    def stop(self):
        if not self.begin:
            print("first obj.start() than obj.stop() last obj")
        else:
            self.end = t.localtime()
            self._calc()
            print("end...")
        
    def _calc(self):
        self.lasted = []
        self.prompt = 'total : '
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        self.begin = 0
        self.end = 0

#t1 = MiTimer()
#t1.start()
#t1.stop()
#t1
