import numpy as np
from tensorflow import keras

def load_weights_from_file(filename):
    weights = []
    with open(filename, "r") as file:
        for line in file:
            weights.append(list(map(float, line.strip().split(','))))
    return weights

weights_path = "model_weights.txt"
loaded_weights = load_weights_from_file(weights_path)

input_data = np.array([[29.0, 1.97, 3.77]])

model = keras.Sequential(
    [
        keras.layers.Input(shape=(3,)),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(1),
    ]
)

model.set_weights(loaded_weights)

prediction = model.predict(input_data)

print("Input:", input_data)
print("Prediction:", prediction)

