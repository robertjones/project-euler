# TODO: pair etc. need to return the card that is in the pair for comparison.

from collections import namedtuple

# Helper functions

def pairs(lst):
    for i in range(len(lst)-1):
        yield (lst[i], lst[i+1])

def kind(hand, number):
    counts = {value: 0 for value in range(14, 1, -1)}
    for card in hand:
        counts[card.value] += 1
    return [value for value, count in counts.items() if count >= number]

# Other functions

Card = namedtuple('Card', ['value', 'suit'])

def hand_gen(text):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return tuple(sorted((Card(values[card[0]], card[1])
                         for card in text.split(" ")), reverse=True))

def hand_rank(hand):
    rank_and_values = (
        royal_flush(hand) or
        straight_flush(hand) or
        four_kind(hand) or
        full_house(hand) or
        flush(hand) or
        straight(hand) or
        three_kind(hand) or
        two_pair(hand) or
        pair(hand) or
        [1])
    return tuple(rank_and_values) + hand

def p1_wins(txt):
    p1_win_sum = 0
    for line in txt:
        p1 = hand_rank(hand_gen(line[:14]))
        p2 = hand_rank(hand_gen(line[15:29]))
        p1_win_sum += 1 if p1 > p2 else 0
        print(line, p1 > p2, p1_win_sum)
    return p1_win_sum

# Hand defintions

def royal_flush(hand):
    rank = 10
    is_rf = flush(hand) and [card.value for card in hand] == [14,13,12,11,10]
    return [rank] if is_rf else False

def straight_flush(hand):
    rank = 9
    return  [rank] if flush(hand) and straight(hand) else False

def four_kind(hand):
    values = kind(hand, 4)
    rank = 8
    return [rank] + values if values else False

def full_house(hand):
    rank = 7
    counts = [0]*15
    for card in hand:
        counts[card.value] += 1
    is_full_house = set(count for count in counts) == set([0, 2, 3])
    return [rank, counts.index(3), counts.index(2)] if is_full_house else False

def flush(hand):
    rank = 6
    return [rank] if all(card.suit == hand[0].suit for card in hand[1:]) else False

def straight(hand):
    rank = 5
    return [rank] if all(a.value - b.value == 1 for a, b in pairs(hand)) else False

def three_kind(hand):
    values = kind(hand, 3)
    rank = 4
    return [rank] + values if values else False

def two_pair(hand):
    rank = 3
    counts = {value: 0 for value in range(14, 1, -1)}
    for card in hand:
        counts[card.value] += 1
    values = [value for value, count in counts.items() if count == 2]
    return [rank] + values if values else False

def pair(hand):
    rank = 2
    return [rank] if kind(hand, 2) else False

print(p1_wins(open('p054_poker.txt')))
