from tensorflow import keras
import numpy as np
import pickle

with open("model.pk", "rb") as f:
    model = pickle.load(f)
X = [[float(input("Temperature: ")), float(input("Voltage: "))]]
predictions = model.predict(X)
for i in range(len(predictions)):
    print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]}")
