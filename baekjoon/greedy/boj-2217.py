# 2217. 로프

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

max_weight = 0
for i in range(n):
    cur_max = ropes[i] * (n-i)
    if max_weight < cur_max:
        max_weight = cur_max

print(max_weight) 