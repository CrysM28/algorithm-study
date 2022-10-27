# 25633. 도미노 넘어뜨리기

n = int(input())
domino = list(map(int, input().split()))

# dp[index] = [개수, 무게]
dp = [[0, 0] for _ in range(n)]
dp[0] = [1, domino[0]]

for i in range(1, n):
    
    # 앞의 모든 도미노 확인
    for j in range(1, i+1):
        # 무게
        if domino[i] <= dp[i-j][1]:
            # 개수
            if dp[i][0] <= dp[i-j][0]:
                dp[i][0] = dp[i-j][0] + 1
                dp[i][1] = dp[i-j][1] + domino[i]

    # 앞 도미노로 못 무너뜨리면 
    if dp[i][0] == 0:
        dp[i][0] = 1
        dp[i][1] = domino[i]

    print(dp)

max_domino = max(list(zip(*dp))[0])
print(max_domino)

