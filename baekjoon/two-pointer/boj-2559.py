# 2559. 수열

N, K = map(int, input().split())
temp = list(map(int, input().split()))

ps = [0] * (N+1)
for i in range(1, N+1):
    ps[i] = ps[i-1] + temp[i-1]


left, right = 1, K
ans = -int(1e9)
while right <= N:
    temp_sum = ps[right] - ps[left-1]
    ans = max(ans, temp_sum)
    left += 1
    right += 1

print(ans)