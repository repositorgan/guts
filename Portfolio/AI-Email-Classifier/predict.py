import pickle


with open('model.pkl', 'rb') as f:
vec, model = pickle.load(f)


email = "this invoice is past due"
pred = model.predict(vec.transform([email]))
print(pred)
