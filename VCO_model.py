import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

X = []
y = []
with open("formatted_data.txt", "r") as f:
    x1, x2, yi = map(float, f.readline().split())
    X.append([x1, x2])
    y.append(yi)

# X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])
# y = np.array([3.0, 5.0, 7.0, 9.0])
X = np.array(X)
y = np.array(y)

model = keras.Sequential(
    [
        layers.Input(shape=(2,)),  # Input layer with 2 neurons (two floats)
        layers.Dense(
            64, activation="relu"
        ),  # Hidden layer with 64 neurons and ReLU activation
        layers.Dense(1),  # Output layer with 1 neuron (single float)
    ]
)

# Compile the model
model.compile(
    optimizer="adam", loss="mean_squared_error"
)  # You can use different optimizers and loss functions based on your problem

# Train the model
model.fit(
    X, y, epochs=1000
)  # You may need to adjust the number of epochs based on your specific problem and data

# Make predictions
predictions = model.predict(X)

# Print the predictions
for i in range(len(predictions)):
    print(
        f"Input: {X[i]}, Expected Output: {y[i]}, Predicted Output: {predictions[i][0]}"
    )
