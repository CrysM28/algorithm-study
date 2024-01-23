# 1010. 다리 놓기

import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ans = math.factorial(M) // math.factorial(M-N) // math.factorial(N)
    print(ans)