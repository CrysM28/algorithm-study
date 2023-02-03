# 2342. Dance Dance Revolution

move = list(map(int, input().split()))
move = move[:-1]

n = len(move)

# dp[i]: i번째에서의 L,R 발의 [위치, 힘]
dp = [[[0, 0]]*2 for _ in range(n)]

dp[0][0] = [move[0], 2]
dp[1][0] = [move[0], 2]
dp[1][1] = [move[1], 2]


for i in range(2, n):
    left_pos = dp[i-1][0][0]
    left_power = dp[i-1][0][1]
    right_pos = dp[i-1][1][0]
    right_power = dp[i-1][1][1]

    next_l_pos = abs(move[i] - left_pos)
    next_r_pos = abs(move[i] - right_pos)

    if next_l_pos == 0:
        next_l_pow = 1
    elif next_l_pos == 2:
        next_l_pow = 4
    else:
        next_l_pow = 3

    if next_r_pos == 0:
        next_r_pow = 1
    elif next_r_pos == 2:
        next_r_pow = 4
    else:
        next_r_pow = 3


    if next_l_pow < next_r_pow:
        dp[i][0] = [move[i], left_power + next_l_pow]
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = [move[i], right_power + next_r_pow]

    #print("==", i, move[i])
    #print(next_l_pos, next_r_pos)


ans = dp[-1][0][1] + dp[-1][1][1]
print(dp)
print(ans)