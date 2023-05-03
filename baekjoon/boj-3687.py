# 3687. 성냥

stick = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# 개수: 숫자
#stick = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


# 51
A = 11

T = int(input())
for _ in range(T):
    n = int(input())

    min_num = int(1e9)
    max_num = 0

    # 최대값
    max_dp = [[0]*(n+1) for _ in range(A)]

    for i in range(A):
        for j in range(n+1):
            if i == 0 or j == 0:
                continue
            print("==")
            print(i, j)
            for idx, s in enumerate(stick):
                print(idx, s)
                if s <= j:
                    print(idx*(10**i))
                    max_dp[i][j] = max(idx*(10**i)+max_dp[i-1][j-s], max_dp[i-1][j])

                else:
                    max_dp[i][j] = max_dp[i-1][j]


    print(*max_dp, sep='\n')

    # while n > 0:
    #     next_line = [0] * 10
    #     for j in range(10):
    #         next_line[j] = max(next_line[j], )

    #     max_dp.append(next_line)





