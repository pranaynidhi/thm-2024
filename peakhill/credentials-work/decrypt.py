import pickle
f = open('creds.pickle', 'rb')
data = pickle.load(f)
print(data)
