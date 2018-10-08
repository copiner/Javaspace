class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
c = CountList(1,3,5,7,9)
d = CountList(2,4,6,8,10)
print(c[1])
print(d[1])

print(c[1] + d[1])

print(c.count)
