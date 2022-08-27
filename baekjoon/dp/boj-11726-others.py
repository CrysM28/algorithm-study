# bottom-up 방식

n = int(input())

t = [0] * 1001
t[1] = 1
t[2] = 2

for i in range(3, 1001):
    t[i] = t[i - 2] + t[i - 1]

print(t[n] % 10007)