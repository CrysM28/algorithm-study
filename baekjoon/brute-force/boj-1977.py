# 1977. 완전제곱수
import math
M = int(input())
N = int(input())

sq = []
for i in range(M, N+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        sq.append(i)

if not sq:
    print(-1)
else:
    print(sum(sq))
    print(sq[0])