import io
import re
import string
f = io.open("./in.txt", "r")
ss = f.readlines()
ss = [s[:-1] if s[-1] == "\n" else s for s in ss]

def has_exactly_two_number_neighbours(m: re.Match, lineNum: int):
    print(m)
    for num in re.finditer(r"\d+", ss[lineNum - 1]):
        print(num)

for row in range(len(ss)):
    line = ss[row]
    starMatches = re.finditer(r"\*", line)
    numberMatches = [re.finditer(r"\d+", ss[row + i]) for i in range(-1, 2)]
        # each m at m.start() is a "*"
        has_exactly_two_number_neighbours(m, row)

