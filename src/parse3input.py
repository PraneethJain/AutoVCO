with open("ok.csv") as f:
    line1, line2 = f.readlines()
    
datas1 = line1.split(",")[1:]
datas2 = line2.split(",")[1:]

with open("data/dataset5.csv", "w") as f:
    for x, y in zip(datas1, datas2):
        try:
            temperature, control_voltage, input_voltage = [float(z.split("=")[-1]) for z in x.split()]
            frequency = float(y)
            if control_voltage < 1.3 or input_voltage == 2.0 or control_voltage > input_voltage:
                continue
            f.write(f"{temperature} {control_voltage} {input_voltage} {frequency}\n")
        except:
            continue