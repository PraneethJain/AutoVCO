from rich import print

with open("data/dataset4.txt") as f:
    inputs, output = f.readlines()

inps = []
outs = []
with open("data/formatted_dataset4.txt", "w") as f:
    for inp, out in zip(inputs.split(","), output.split(",")):
        f.write(
            f"{' '.join([val.split('=')[-1] for val in inp.split()])} {out.strip()}\n"
        )
