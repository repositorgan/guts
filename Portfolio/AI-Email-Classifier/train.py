from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


emails = ["invoice due", "meeting tomorrow", "limited time offer"]
labels = ["finance", "work", "marketing"]


vec = CountVectorizer()
X = vec.fit_transform(emails)


model = MultinomialNB()
model.fit(X, labels)


with open('model.pkl', 'wb') as f:
pickle.dump((vec, model), f)
