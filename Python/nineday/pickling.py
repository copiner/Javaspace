#pickle
import pickle
d = dict(name='francis', age=18, score=75)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)
