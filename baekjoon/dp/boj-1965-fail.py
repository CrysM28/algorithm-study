# 1965. 상자넣기

n = int(input())
box = list(map(int, input().split()))

# dp[이전 box의 idx][현 최대 val]
dp = [[0] * n for _ in range(2)]
dp[0][0] = 0
dp[1][0] = 1


for i in range(1, n):
    idx1 = dp[0][i-1]
    idx2 = i-1
    val1 = 0
    val2 = 0

    if box[i] > box[idx1]:
        val1 = dp[1][idx1] + 1
    if box[i] > box[idx2]:
        val2 = dp[1][idx2] + 1
    
    print(i)
    print(val1, val2)
    print(idx1, idx2)
    
    if val1 > val2:
        dp[0][i] = idx1
        dp[1][i] = val1
    else:
        dp[0][i] = idx2
        dp[1][i] = val2


print(*dp, sep='\n')




# for i in range(1, n):
#     j = i
#     while j >= 0:
#         if box[i] > box[j]:
#             #print(box[i], box[j])
#             break
#         j -= 1

#     k = i
#     if box[i] > box[i-1]:
#         k -= 1
    
#     dp[i] = max(dp[j]+1, dp[k]+1)


# print(dp)
# print(max(dp))

