import matplotlib.pyplot as plt
from matplotlib import cm

temperatures = []
input_voltages = []
output_frequencies = []
data = {} # mapping from control voltage to list of temperatures, input voltages and output frequencies
with open("data/formatted_dataset4.txt", "r") as f:
    for line in f.readlines():
        try:
            temperature, control_voltage, input_voltage, output_frequency = map(float, line.split())
            if 1 < control_voltage <= 3.6 and output_frequency < 1000:
                if (control_voltage in data):
                    data[control_voltage][0].append(temperature)
                    data[control_voltage][1].append(input_voltage)
                    data[control_voltage][2].append(output_frequency)
                else:
                    data[control_voltage] = [[temperature], [input_voltage], [output_frequency]]
        except ValueError:
            continue



for control_voltage, vals in data.items():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    X, Y, Z = vals
    surf = ax.plot_trisurf(X, Y, Z, cmap=cm.jet, linewidth=0)
    fig.colorbar(surf)


    fig.tight_layout()

    plt.savefig(f"plots/3D{control_voltage}.png")
