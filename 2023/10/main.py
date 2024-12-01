import io
import enum
from typing import *
f = io.open("./in.txt", "r")
ss = f.readlines()
ss = [s.replace("\n", "") for s in ss]
ss = [s.split() for s in ss]

class Node:
    def __init__(self, x: int, y: int, symbol: str) -> None:
        self.x = x
        self.y = y
        self.symbol = symbol

    def can_connect_to(self, other: 'Node'):
        match self.symbol, other.symbol:
            case _, 'S':
                return True
            case 'S', _:
                return True
            