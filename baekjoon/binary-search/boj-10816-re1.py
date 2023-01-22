# 10816. 숫자 카드 2
## 1044 -> 888

import sys
from collections import defaultdict
input = sys.stdin.readline

cards = defaultdict(int)

n = int(input())
sg_cards = list(map(int, input().split()))

for s in sg_cards:
    cards[s] += 1

m = int(input())
input_cards = list(map(int, input().split()))

for i in input_cards:
    print(cards[i], end=" ")