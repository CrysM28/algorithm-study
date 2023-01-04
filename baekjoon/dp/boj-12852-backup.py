# 12852. 1로 만들기 2
from collections import defaultdict

n = int(input())
dp = defaultdict(list)

ans = []

def find(num, arr):
    global ans
    print(num, arr)
    if num == 1:
        ans = arr[::]
        print(ans)
        return

    if ans:
        return
    
    if num%3 == 0:
        arr.append(num//3)
        find(num//3, arr)
        arr.pop()   
    
    if num%2 == 0:
        arr.append(num//2)
        find(num//2, arr)
        arr.pop()

    arr.append(num-1)
    find(num-1, arr)
    arr.pop()





find(n, [])

#dp[n] = 1
# for i in range(n, 1, -1):
#     dp[i-1] = dp[i] + 1

# print(dp[0])
# print(dp)
# for i in range(2, n+1):
#     dp[i] = dp[i-1].append(i)
#     # if i % 3 == 0:
#     #     dp[i] = min(dp[i], dp[i // 3] + 1)
#     # if i % 2 == 0:
#     #     dp[i] = min(dp[i], dp[i // 2] + 1)

# for i in range(1, n+1):
#     print(i, dp[i])
# #print(dp)