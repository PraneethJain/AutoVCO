from tensorflow import keras
import numpy as np
import pickle
import serial

with open("model.pk", "rb") as f:
    model = pickle.load(f)
while True:
    b = input()
    X = [list(map(float, b.split()))]
    predictions = model.predict(X)
    for i in range(len(predictions)):
        print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]}")
