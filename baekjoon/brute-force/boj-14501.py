# 14501. 퇴사

N = int(input())
time = []
price = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)


max_price = 0
visited = [0] * N

def dfs(v, cur_price):
    global max_price
    visited[v] = 1
    cur_price += price[v]
    for next_v in range(v+1, N):
        if v + time[v] <= next_v and next_v + time[next_v] <= N:
            dfs(next_v, cur_price)
            visited[next_v] = 0
    max_price = max(max_price, cur_price)

for i in range(N):
    if i + time[i] <= N:
        dfs(i, 0)

print(max_price)
