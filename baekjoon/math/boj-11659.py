# 11659. 구간 합 구하기 4
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
s = defaultdict(int)

# 구간합 배열 만들기
for i in range(1, N+1):
    s[i] = s[i-1] + a[i-1]

# 구간합 구하기
for _ in range(M):
    x, y = map(int, input().split())
    print(s[y] - s[x-1])