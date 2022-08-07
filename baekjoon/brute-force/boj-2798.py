# 블랙잭
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

card_3 = combinations(cards, 3)
blackjack = 0

for c in card_3:
    sum = c[0] + c[1] + c[2]
    if sum <= m and sum > blackjack:
        blackjack = sum

print(blackjack)