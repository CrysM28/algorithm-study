# 17626. Four Squares
from collections import defaultdict

n = int(input())
dp = defaultdict(int)
MAX = 4

dp[1] = 1
dp[2] = 2
dp[3] = 3

cur_num = 2
cur_pow = cur_num**2

for i in range(4, n + 1):
    # 어떤 수의 제곱이면 그거 하나로 표현가능
    if i == cur_pow:
        dp[i] = 1
        cur_num += 1
        cur_pow = cur_num**2

    # dp[제곱수] + dp[전체-제곱수] 끼리만 비교해도 최소 알 수 있음
    else:
        dp[i] = MAX

        tmp_num = cur_num - 1
        while tmp_num > 0:
            tmp_pow = tmp_num**2

            dp[i] = min(dp[i], dp[tmp_pow] + dp[i - tmp_pow])

            ## min 대신 쓰면 472 -> 424로 50ms 정도 줄어들긴 함
            #if dp[i] > dp[tmp_pow] + dp[i - tmp_pow]:
            #    dp[i] = dp[tmp_pow] + dp[i - tmp_pow]

            tmp_num -= 1

            # 최소 개수 찾았으면 바로 끝내서 시간 줄이기
            if dp[i] == 2:
                break

#print(dp)
print(dp[n])