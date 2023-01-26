# 9375. 패션왕 신해빈
from collections import defaultdict

for _ in range(int(input())):
    clothes = defaultdict(list)

    n = int(input())
    for _ in range(n):
        a, b = input().split()
        clothes[b].append(a)
    
    ans = 1
    for cloth in clothes.values():
        ans *= (len(cloth) + 1)

    print(ans-1)