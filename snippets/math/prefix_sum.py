# 누적합
## s[x~y] = s[y] - s[x-1]

n = int(input())
a = [0] + list(map(int, input().split())) 
s = [0] * (n + 1)

# 구간합 배열 만들기
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

# 구간합 구하기
x, y = map(int, input().split())
prefix_sum = s[y] - s[x-1]
