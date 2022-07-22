# 큰 수의 법칙
n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
answer = 0
counter = k

for i in range(m):
    if counter == 0:
        answer += a[1]
        counter = k
    else:
        answer += a[0]
        counter -= 1

print(answer)
