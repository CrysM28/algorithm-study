# 12865. 평범한 배낭

# 물품의 수, 최대 무게
n, capacity = map(int, input().split())

# 물건 (무게, 가치)
things = []
for _ in range(n):
    things.append(list(map(int, input().split())))


def zero_one_knapsack(cargo):
    # 짐의 가치를 저장할 dp 테이블
    dp = []

    for i in range(len(cargo) + 1):
        dp.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                dp[i].append(0)
            elif cargo[i - 1][0] <= c:
                dp[i].append(
                    max(
                        cargo[i - 1][1] + dp[i - 1][c - cargo[i - 1][0]],
                        dp[i - 1][c]
                    ))
            else:
                dp[i].append(dp[i-1][c])

    return dp[-1][-1]

answer = zero_one_knapsack(things)
print(answer)