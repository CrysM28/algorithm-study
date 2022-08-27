# 9095. 1,2,3 더하기
from collections import defaultdict

# 기본값
dp = defaultdict(int)
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 이 규칙만 찾아내면 쉬운 문제...
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
    



