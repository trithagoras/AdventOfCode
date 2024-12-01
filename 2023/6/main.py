import math

races = {
    # 62: 553,
    # 64: 1010,
    # 91: 1473,
    # 90: 1074
    62649190: 553101014731074
}

def f(a, b, c):
    return (-b + math.sqrt(b**2 - (4 * a * c)))/(2*a), (-b - math.sqrt(b**2 - (4 * a * c)))/(2*a)

total = 1

for maxX, minY in races.items():
    x1, x2 = f(-1, maxX, -minY)
    x1 = math.ceil(x1)
    x2 = math.floor(x2)
    amt = (x2 - x1) + 1
    total *= amt
print(total)