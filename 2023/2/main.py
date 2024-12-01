import io
import string
f = io.open("./in.txt", "r")
ss = f.readlines()

POSSIBLE_CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

RESULT = 0

def is_game_possible(line: str) -> bool:
    subgames = line.split(":")[1].split(";")
    for subgame in subgames:
        for num_cubes in subgame.split(','):
            num, color = num_cubes.split()
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True

for index, line in enumerate(ss):
    if is_game_possible(line):
        print(f"Game {index + 1} is possible")
        RESULT += (index + 1)

print(RESULT)