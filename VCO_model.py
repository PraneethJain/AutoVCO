import numpy as np
import tensorflow as tf
from tensorflow import keras

X = []
y = []
with open("formatted_data.txt", "r") as f:
    x1, x2, yi = map(float, f.readline().split())
    X.append([x1, x2])
    y.append(yi)

X = np.array(X)
y = np.array(y)

model = keras.Sequential(
    [
        keras.layers.Input(shape=(2,)),  # Input layer with 2 neurons (two floats)
        keras.layers.Dense(
            64, activation="relu"
        ),  # Hidden layer with 64 neurons and ReLU activation
        keras.layers.Dense(1),  # Output layer with 1 neuron (single float)
    ]
)

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, y, epochs=1000)
predictions = model.predict(X)
for i in range(len(predictions)):
    print(
        f"Input: {X[i]}, Expected Output: {y[i]}, Predicted Output: {predictions[i][0]}"
    )
