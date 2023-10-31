import csv
import matplotlib.pyplot as plt

with open(f"data/temperature_dataset.csv", newline="") as csvfile:
    row1, row2 = csv.reader(csvfile, delimiter=",")
    row1 = row1[1:]
    row2 = row2[1:]

X = []
Y = []
for parameters, res in zip(row1, row2):
    temperature, _ = [s.split("=")[-1] for s in parameters.split()]
    if res:
        X.append(float(temperature))
        Y.append(float(res))

plt.plot(X, Y)
plt.xlabel("Temperature (Celsius)")
plt.ylabel("Frequency (Hz)")
# plt.show()
plt.savefig("plots/2D.png")
