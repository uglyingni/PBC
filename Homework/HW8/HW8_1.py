from collections import Counter
import math


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def calculate_score(cards):
    rank_list = []
    suit_list = []
    number_list = []
    for card in cards:
        rank_list.append(card.rank)
        suit_list.append(card.suit)

    for rank in rank_list:
        if rank == 'A':
            number_list.append(1)
        elif rank == 'J':
            number_list.append(11)
        elif rank == 'Q':
            number_list.append(12)
        elif rank == 'K':
            number_list.append(13)
        else:
            number_list.append(int(rank))

    # 計算是否有 A，如果有則加 5 分
    score = 0

    for card in cards:
        if card.rank == 'A':
            score += 5

    # pair
    ranks = Counter(rank_list)
    for rank, num in ranks.items():
        com = math.comb(num, 2)
        score += 10 * com

    # 計算是否為同花，如果是則加 30 分
    suits = Counter(suit_list)
    if len(suits) == 1:
        score += 30

    # 順子
    sorted_num = sorted(number_list)
    if sorted_num[0] == 1 and sorted_num[4] == 13:
        for i, num in enumerate(sorted_num):
            if num == 13:
                sorted_num[i] = 0
            elif num == 12:
                sorted_num[i] = -1
            elif num == 11:
                sorted_num[i] = -2
            elif num == 10:
                sorted_num[i] = -3

    diff = sorted(sorted_num)[4] - sorted(sorted_num)[0]
    if (len(ranks) == 5) and (diff == 4):
        score += 50

    # 葫蘆
    if set(ranks.values()) == {2, 3}:
        score += 80

    # # 計算是否為四條，如果是則加 100 分
    if set(ranks.values()) == {1, 4}:
        score += 100

    # 計算是否為同花順，如果是則加 300 分
    if (len(suits) == 1) and (len(ranks) == 5) and (diff == 4):
        score += 300

    return score


suit = input().split(",")
rank = input().split(",")
cards = []
for i in range(5):
    card = Card(suit[i], rank[i])
    cards.append(card)

print(calculate_score(cards))
