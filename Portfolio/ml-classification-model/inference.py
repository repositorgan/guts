from model_utils import load_model

model = load_model()
sample = [[5.1, 3.5, 1.4, 0.2]]
pred = model.predict(sample)
print(pred)
