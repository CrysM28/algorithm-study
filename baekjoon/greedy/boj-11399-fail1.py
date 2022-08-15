# 11399. ATM
## 메모리 초과 -> permutations 때문인듯
from itertools import permutations

n = int(input())  # 사람 수
time = list(map(int, input().split()))  # 인출 시간
order = [x for x in range(n)]  # 인출 순서
order = list(permutations(order, n))  # 인출 순서 가능한 모든 순열
min_t = int(1e6)

# 모든 순서에 대해 최소값 계산
for o in order:
    #print(o, len(o))
    this_t = 0
    for i, p in enumerate(o):
        #print(time[p], n-i)
        this_t += time[p] * (n-i)
    min_t = min(min_t, this_t)

print(min_t)