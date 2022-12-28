# 1417. 국회의원 선거
import heapq as h

N = int(input())
dasom = int(input())
buy = 0

# 최대힙
votes = []
for _ in range(N-1):
    h.heappush(votes, -int(input()))


while votes:
    vote = -h.heappop(votes)
    if dasom > vote:
        break

    buy += 1
    dasom += 1
    h.heappush(votes, -(vote-1))

#print(dasom)
print(buy)