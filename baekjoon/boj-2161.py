from collections import deque

n = int(input())

cards = deque([i for i in range(1, n+1)])
#print(cards)

while len(cards) > 1:
    first = cards.popleft()
    second = cards.popleft()

    print(first, end = ' ')
    cards.append(second)

print(cards[0])