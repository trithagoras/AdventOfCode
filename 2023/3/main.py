# solution notes:
"""
* Find each number in each row, taking note of the start index and the 'length' of the number.
* for each number, check the surrounding neighbours - check_for_neighbour(idx, length)
"""

import io
import re
import string
f = io.open("./in.txt", "r")
ss = f.readlines()
ss = [s[:-1] if s[-1] == "\n" else s for s in ss]

def has_neighbour(m: re.Match, row_num: int):
    for y in range(row_num - 1, row_num + 2):
        for x in range(m.start() - 1, m.end() + 1):
            y = min(y, len(ss) - 1)
            x = min(x, len(ss[0]) - 1)
            if ss[y][x] != "." and ss[y][x] not in string.digits:
                return True
            
    return False

count = 0
for row in range(len(ss)):
    line = ss[row]
    for m in re.finditer(r"\d+", line):
        if has_neighbour(m, row):
            val = int(line[m.start():m.end()])
            count += val

print(count)