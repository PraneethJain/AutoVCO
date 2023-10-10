import csv
from rich import print

with open("data.csv", newline='') as csvfile:
    row1, row2 = csv.reader(csvfile, delimiter=',')
    row1 = row1[1:]
    row2 = row2[1:]

with open("formatted_data.txt", "w") as f:
    for parameters, res in zip(row1, row2):
        temperature, voltage = [s.split('=')[-1] for s in parameters.split()]
        if res:
            f.write(f"{temperature} {voltage} {res}\n")
