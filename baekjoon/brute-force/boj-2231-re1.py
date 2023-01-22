# 2231. 분해합
## 복습

n = int(input())
ans = 0
start = max(1, n-9*len(str(n)))

for i in range(start, n+1):
    s = i + sum(map(int, str(i)))

    if s == n:
        ans = i
        break

print(ans)