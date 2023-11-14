from tensorflow import keras
import numpy as np
import pickle

X = []
y = []
with open("data/formatted_dataset4.txt", "r") as f:
    for line in f.readlines():
        try:
            x1, x2, x3, yi = map(float, line.split())
            X.append([x1, x2, x3])
            y.append(yi)
        except ValueError:
            continue

X = np.array(X)
y = np.array(y)

model = keras.Sequential(
    [
        keras.layers.Input(shape=(3,)),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(1),
    ]
)

model.compile(optimizer="adam", loss="mape")
model.fit(X, y, epochs=250)
with open("model.pk", "wb") as f:
    pickle.dump(model, f)