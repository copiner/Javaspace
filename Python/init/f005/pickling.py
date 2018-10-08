import pickle
melist = [123, 3.14, "francis", ['other', 'list']]
pickle_file = open("melist.pkl",'wb')
pickle.dump(melist, pickle_file)
pickle_file.close()

pickling_file = open("melist.pkl",'rb')
milist = pickle.load(pickling_file)
print(milist)

#weather
