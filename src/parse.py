import csv
from rich import print

for i in range(1, 3):
    with open(f"data/dataset{i}.csv", newline="") as csvfile:
        row1, row2 = csv.reader(csvfile, delimiter=",")
        row1 = row1[1:]
        row2 = row2[1:]

    with open(f"data/formatted_dataset{i}.txt", "w") as f:
        for parameters, res in zip(row1, row2):
            temperature, voltage = [s.split("=")[-1] for s in parameters.split()]
            if res:
                f.write(f"{temperature} {voltage} {res}\n")
