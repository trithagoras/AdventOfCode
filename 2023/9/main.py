import io
from typing import *
f = io.open("./in.txt", "r")
ss = f.readlines()
ss = [s.replace("\n", "") for s in ss]
ss = [s.split() for s in ss]

total = 0

for ls in ss:
    xs = [int(x) for x in ls]

    diffs = [xs[i] - xs[i-1] for i in range(1, len(xs))]
    layers = [xs] + [diffs]
    
    while any([x for x in diffs if x != 0]):
        prevLayer = layers[-1]
        diffs = [prevLayer[i] - prevLayer[i-1] for i in range(1, len(prevLayer))]
        layers += [diffs]

    newNumber = 0

    layers.reverse()
    for layer in layers:
        layer.reverse()

    for layer in layers[1:]:
        lastNumber = layer[-1]
        newNumber += lastNumber
    
    total += newNumber

print(total)