import io
from typing import *
f = io.open("./in.txt", "r")
ss = f.readlines()
ss = [s.replace("\n", "") for s in ss]

STEPS = "LRRLRLRRLRRRLRLRLRRLRRRLRRRLRRLRRRLRLRLRLRLRLRLRRRLRRLRRRLLLLRRRLRLLLRRRLLRLLRRRLRRRLRLRRLRRRLRRRLLRRRLRLRRRLLRRRLRLLRRRLRRLLRLRLRLRRRLRLLRLRLRRRLRLLRLRLRRRLLRRRLRRLRRRLRLRRLRLRRLRLRRLRRRLLRRRLLLRRRLLRRLRRLRRLRLLRRLRRRLRRLRLRLRRLRRLLLRRLRLRRRLRRRLRRRLLLRLRRRLLRRRLRLLRRRR"

# cleaning data
MAP = {}
for s in ss:
    i = s.find("(")
    l = (s[i+1:-1]).split(", ")
    MAP[s[:3]] = l


poss = [k for k in MAP.keys() if k[2] == "A"]

# count = 0

def move(x: str, step: str):
    v = MAP[x]
    next = v[0] if step == "L" else v[1]
    return next

# while any([x[2] != "Z" for x in poss]):
#     for step in STEPS:
#         if all([x[2] == "Z" for x in poss]):
#             break
#         if len([x for x in poss if x[2] == "Z"]) > 2:
#             print(f"{poss}")
#         poss = [move(x, step) for x in poss]
#         count += 1

# print(f"{poss} was reached in {count} moves!")


pos = "RCA"
target = pos
print(pos)

i = 0
L = len(STEPS)
while True:
    stepIdx = i % L
    step = STEPS[stepIdx]

    pos = move(pos, step)
    # print(pos)

    if pos[-1] == "Z":
        print(f"{pos} reached after {i} steps.")
        # break

    i += 1