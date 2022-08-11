# 10814. 나이순 정렬

n = int(input())
members = []
for _ in range(n):
    a, b = input().split() 
    members.append([int(a), b])
    
members.sort(key = lambda x: x[0])

for m in members:
    print(*m)

