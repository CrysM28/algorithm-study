# 11399. ATM

n = int(input())
ppl = sorted(list(map(int, input().split())))

time = 0 

for i, t in enumerate(ppl):
    time += (n-i) * t

print(time)

