from tensorflow import keras
import numpy as np
import pickle
import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rich import print

with open("model.pk", "rb") as f:
    model = pickle.load(f)


# def listener(event):
# data = curRef.get();
# print(data)
# actual_frequency = data["frequency"]
actual_frequency = 493.0
# X = [[data["temperature"], float(input("Control Voltage: ")), data["voltage"]]]
X = [[29.3, 1.96, 3.70]]
predictions = model.predict(X)
for i in range(len(predictions)):
    print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]}")
    predicted_frequency = predictions[i][0]           
    percentage_error = (predicted_frequency - actual_frequency) / actual_frequency * 100
    print(f"{abs(percentage_error):.2f}% frequency error")
    if (abs(percentage_error) < 5):
        continue


    current_resistance = float(input("Enter resistance: "))
    new_resistance = current_resistance*(100 - percentage_error)/100
    if percentage_error > 0:
        print(f"Decrease resistance by {abs(percentage_error):.2f}%")
    else:
        print(f"Increase resistance by {abs(percentage_error):.2f}%")
    print(f"New resistance: {new_resistance}")
        

# SERVICE_ACCOUNT_JSON_PATH = "/home/praneeth/Downloads/firebasekey.json"
# cred = credentials.Certificate(SERVICE_ACCOUNT_JSON_PATH)
# firebase_admin.initialize_app(
#     cred,
#     {
#         "databaseURL": "https://vco-ml-default-rtdb.asia-southeast1.firebasedatabase.app"
#     },
# )
# curRef = db.reference("cur")
# curRef.listen(listener)
