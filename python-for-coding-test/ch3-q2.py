# 큰 수의 법칙
## 효율 좋게 바꿔보기

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = 0

for i in range(m):
    if ((i+1) % k) == 0:
        answer += a[-2]
    else:
        answer += a[-1]

print(answer)
