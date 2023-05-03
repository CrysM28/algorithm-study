# 1965. 상자넣기
## LIS로 풀수 있다고 함
## 이 방법은 O(N^2) 풀이
n = int(input())
box = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(max(dp))