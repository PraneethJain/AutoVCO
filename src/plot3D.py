import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm

X = []
Y = []
Z = []
with open("data/formatted_dataset3.txt", "r") as f:
    for line in f.readlines():
        try:
            x1, x2, yi = map(float, line.split())
            if 1 < x2 <= 3.6 and yi < 1000:
                X.append(x1)
                Y.append(x2)
                Z.append(yi)
        except ValueError:
            continue


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

surf = ax.plot_trisurf(X, Y, Z, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)


fig.tight_layout()

# plt.show()
plt.savefig("3D.png")
