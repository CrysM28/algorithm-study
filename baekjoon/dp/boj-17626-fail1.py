# 17626. Four Squares
import math
INF = int(1e9)


def solve(x):
    # if dp[x] < INF:
    #     return dp[x]

    for sq in squares:
        if sq < x:
            dp[x] = min(dp[x], 1 + solve(x - sq))
            print(dp[:n+1])
        else:
            break

    return dp[x]


n = int(input())
dp = [INF] * 50001
squares = []

# 제곱 먼저
for i in range(1, int(math.sqrt(n)) + 1):
    dp[i**2] = 1
    squares.append(i**2)

squares = squares[::-1]

solve(n)
print(dp[n])
print(dp[:n+1])

