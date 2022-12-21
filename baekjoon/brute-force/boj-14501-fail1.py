# 14501. 퇴사
## 그냥 브루트포스 하려고 했는데 dfs 쓰는게 편해보임
N = int(input())
time = []
price = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)

max_price = 0
for i in range(N):
    print("==", i)
    cur_price = 0
    j = i
    while j < N:
        if j + time[j] > N:
            break
        
        cur_price += price[j]
        print(j, cur_price)
        j += time[j]

    print(cur_price)

    max_price = max(max_price, cur_price)

print(max_price)