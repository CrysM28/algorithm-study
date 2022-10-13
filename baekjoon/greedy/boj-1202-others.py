import sys
import heapq

N, K = map(int, input().split())

## 보석[무게] = 가격 으로 해서 인덱스 접근으로 시간 줄임
max_mass = 1000000
mass = [[] for _ in range(max_mass+1)]

for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    mass[M].append(V)

bag = []
for _ in range(K):
    C = int(sys.stdin.readline())
    C = min(C, max_mass)
    bag.append(C)
bag.sort()

max_heap = []
now = 0
ans = 0
for k in bag:
    while now <= k:
        for value in mass[now]:
            heapq.heappush(max_heap, -value)
        now += 1
    
    if max_heap:
        v = heapq.heappop(max_heap)
        ans += -v

print(ans)