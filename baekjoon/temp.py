
n = int(input())
st = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.insert(len(ans)-st[i], i+1)
    
print(*ans)