import io
import enum
from typing import *
import functools
f = io.open("./in.txt", "r")
ss = f.readlines()

hands = []
bids = []
M = {}

class Type(enum.Enum):
    FIVE_OAK = 6
    FOUR_OAK = 5
    FULL_HOUSE = 4
    THREE_OAK = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

def compare_hands_type(left: str, right: str) -> int:
    tleft = get_type(left)
    tright = get_type(right)
    if tleft.value == tright.value:
        return 0
    if tleft.value < tright.value:
        return -1
    return 1

def compare_cards_rank(left: str, right: str) -> int:
    order = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
    if (order[left] == order[right]):
        return 0
    if (order[left] > order[right]):
        return 1
    return -1

def compare_hands_rank(left: str, right: str):
    for i in range(len(left)):
        comp = compare_cards_rank(left[i], right[i])
        if comp == 0:
            continue
        if comp == 1:
            return 1
        return -1
    return 0

def get_type(hand: str) -> Type:
    cards = [c for c in hand]
    cards.sort()

    match cards:
        case [a, b, c, d, e]:
            if a == b == c == d == e:
                return Type.FIVE_OAK
            if a == b == c == d or b == c == d == e:
                return Type.FOUR_OAK
            if a == b == c and d == e or a == b and c == d == e:
                return Type.FULL_HOUSE
            if a == b == c or b == c == d or c == d == e:
                return Type.THREE_OAK
            if a == b and c == d or a == b and d == e or b == c and d == e:
                return Type.TWO_PAIR
            if a == b or b == c or c == d or d == e:
                return Type.ONE_PAIR
            return Type.HIGH_CARD

def main():
    for s in ss:
        hand, bid = s.split()
        hands.append(hand)
        bids.append(bid)
        M[hand] = bid

    # group by type first
    fioak = [hand for hand in hands if get_type(hand) == Type.FIVE_OAK]
    foak = [hand for hand in hands if get_type(hand) == Type.FOUR_OAK]
    full = [hand for hand in hands if get_type(hand) == Type.FULL_HOUSE]
    toak = [hand for hand in hands if get_type(hand) == Type.THREE_OAK]
    twop = [hand for hand in hands if get_type(hand) == Type.TWO_PAIR]
    op = [hand for hand in hands if get_type(hand) == Type.ONE_PAIR]
    hc = [hand for hand in hands if get_type(hand) == Type.HIGH_CARD]

    ls = [fioak, foak, full, toak, twop, op, hc]

    # sort each group by rank
    for l in ls:
        l.sort(key=functools.cmp_to_key(compare_hands_rank), reverse=True)

    finalOrder = fioak + foak + full + toak + twop + op + hc

    totalWinnings = 0
    for i in range(len(finalOrder)):
        rank = len(finalOrder) - i
        card = finalOrder[i]
        bid = M[card]
        winning = int(bid) * rank

        totalWinnings += winning
        print(f"{card} is rank {rank}, with an original bid of {bid} and a final winning of {winning}. The total winning is now {totalWinnings}.")

main()
