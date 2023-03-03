# 17425. 약수의 합

n = int(input())
answer = 0

for i in range(1, n+1):
    print(i, i * (n//i))
    answer += i * (n//i)

print(answer)