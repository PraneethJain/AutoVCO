from tensorflow import keras
import numpy as np
import pickle
import serial


with open("model.pk", "rb") as f:
    model = pickle.load(f)
ser = serial.Serial("COM11", 9600)
while True:
    b = ser.readline()
    X = [list(map(float, b.split()))]
    # X = [[float(input("Temperature: ")), float(input("Voltage: "))]]
    predictions = model.predict(X)
    for i in range(len(predictions)):
        print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]}")
