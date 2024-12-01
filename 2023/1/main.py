import io
import string
f = io.open("./in.txt", "r")
ss = f.readlines()

sum = 0

# 2 pointer lookahead
for s in ss:
    num1 = 0
    num2 = 0
    for c in s:
        if c in string.digits:
            num1 = int(c)
            break
    for c in s[::-1]:
        if c in string.digits:
            num2 = int(c)
            break
    num = num1 * 10 + num2
    sum += num

print(sum)
