# 1715. 카드 정렬하기
import heapq as h

N = int(input())
cards = [int(input()) for _ in range(N)]
h.heapify(cards)

answer = 0

for _ in range(N-1):
    c1 = h.heappop(cards)
    c2 = h.heappop(cards)

    answer += c1+c2
    h.heappush(cards, c1+c2)

print(answer)

