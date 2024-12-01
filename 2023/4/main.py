import io
# import re
f = io.open("./in.txt", "r")
ss = f.readlines()

totalScore = 0

winnings = []
pools = []

# clean up
for s in ss:
    if s[-1] == "\n":
        s = s[:-1]
    s = s[s.find(": ")+2:]
    winning, pool = s.split("| ")

    winning = winning.split()
    pool = pool.split()

    winnings.append(winning)
    pools.append(pool)

