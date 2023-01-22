def check(list, num):
    res = [0, 0]
    ad = 0
    for target in list:
        for i in target[num:num + 8]:
            if i == ad:
                res[0] += 1
            elif i == ad ^ 1:
                res[1] += 1
            ad ^= 1
        ad ^= 1
    return max(res)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = [[1 if x == "W" else 0 for x in input().strip()] for x in range(n)]
score = 0

for i in range(n - 7):
    for j in range(m - 7):
        tempScore = check(li[i:i + 8], j)
        if tempScore > score:
            score = tempScore

print(64 - score)
