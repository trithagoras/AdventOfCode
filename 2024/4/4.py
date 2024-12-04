f = open('input.txt').read()
lines = f.splitlines()

windows = [
    [
        "XMAS",
        "....",
        "....",
        "...."
    ],
    [
        "SAMX",
        "....",
        "....",
        "...."
    ],
    [
        "X...",
        "M...",
        "A...",
        "S..."
    ],
    [
        "S...",
        "A...",
        "M...",
        "X..."
    ],
    [
        "X...",
        ".M..",
        "..A.",
        "...S"
    ],
    [
        "S...",
        ".A..",
        "..M.",
        "...X"
    ],
    [
        "...S",
        "..A.",
        ".M..",
        "X..."
    ],
    [
        "...X",
        "..M.",
        ".A..",
        "S..."
    ]
]

windowsPart2 = [
    [
        "M.M",
        ".A.",
        "S.S"
    ],
    [
        "M.S",
        ".A.",
        "M.S"
    ],
    [
        "S.M",
        ".A.",
        "S.M"
    ],
    [
        "S.S",
        ".A.",
        "M.M"
    ]
]

def checkMatch(src, window, pos, maxHits):
    hits = 0
    for r in range(len(window)):
        if pos[0] + r >= len(src):
            continue
        for c in range(len(window[0])):
            if pos[1] + c >= len(src[0]):
                continue
            if window[r][c] == '.':
                continue
            if window[r][c] != src[pos[0] + r][pos[1] + c]:
                return False
            hits += 1
    return hits >= maxHits


def part1():
    matches = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            pos = (row, col)
            for window in windows:
                if checkMatch(lines, window, pos, 4):
                    matches += 1

    print(matches)

def part2():
    matches = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            pos = (row, col)
            for window in windowsPart2:
                if checkMatch(lines, window, pos, 5):
                    matches += 1

    print(matches)

part1()
part2()