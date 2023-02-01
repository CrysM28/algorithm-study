# 2166. 다각형의 면적

N = int(input())
x, y = [], []

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

ans = 0
for i in range(N):
    ans += (x[i] * y[i+1]) - (x[i+1] * y[i])

print(round(abs(ans)/2, 1))