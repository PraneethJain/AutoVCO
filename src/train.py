from tensorflow import keras
import numpy as np
import pickle

X = []
y = []
with open("data/formatted_dataset3.txt", "r") as f:
    for line in f.readlines():
        try:
            x1, x2, yi = map(float, line.split())
            if 1 <= x2 <= 3.6 and yi < 1000:
                X.append([x1, x2])
                y.append(yi)
        except ValueError:
            continue

X = np.array(X)
y = np.array(y)

model = keras.Sequential(
    [
        keras.layers.Input(shape=(2,)),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(10, activation="relu"),
        keras.layers.Dense(1),
    ]
)

model.compile(optimizer="adam", loss="mape")
model.fit(X, y, epochs=1000)
with open("model.pk", "wb") as f:
    pickle.dump(model, f)
