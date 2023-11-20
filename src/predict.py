from tensorflow import keras
import numpy as np
import pickle
from rich import print

with open("model.pk", "rb") as f:
    model = pickle.load(f)


actual_frequency = float(input("Actual Frequency: "))
X = [
    [
        float(input("Temperature: ")),
        float(input("Control Voltage: ")),
        float(input("Input Voltage: ")),
    ]
]
predictions = model.predict(X)
for i in range(len(predictions)):
    print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]}")
    predicted_frequency = predictions[i][0]
    percentage_error = (predicted_frequency - actual_frequency) / actual_frequency * 100
    print(f"{abs(percentage_error):.2f}% frequency error")
    if abs(percentage_error) < 5:
        continue

    current_resistance = float(input("Enter resistance: "))
    new_resistance = current_resistance * (100 - percentage_error) / 100
    if percentage_error > 0:
        print(f"Decrease resistance by {abs(percentage_error):.2f}%")
    else:
        print(f"Increase resistance by {abs(percentage_error):.2f}%")
    print(f"New resistance: {new_resistance}")
