#实例属性、 类属性
class C:
    def getNum():
        print("num...")

C.getNum()

b = C()
#b.getNum()


class Point:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def getXY(self):
        print(self.x, self.y)

d = Point()
print(d.__dict__)
print(Point.__dict__)

d.setXY(4,5) #d.setXY(d, 4, 5)

print(d.__dict__)
print(Point.__dict__)

del Point
#e = Point()

d.getXY()



