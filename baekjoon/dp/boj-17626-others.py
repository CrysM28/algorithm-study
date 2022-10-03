# 472ms -> 144ms 로 내거보다 4배정도 빠름

import sys

input = lambda: sys.stdin.readline().rstrip()


def solution_017626():
    n = int(input())

    dp = [0] * (n + 1)


    ## 제곱수면 dp 돌릴필요 없이 빨리 끝내는 것도 좋은듯 훨씬 적은 시간에 끝낼 수 있음
    # 1개의 제곱 수로 나타낼 수 있는 숫자들의 인덱스에 해당하는 값을 1로 초기화 시킨다.
    for i in range(1, int(n ** .5) + 1):
        dp[i ** 2] = 1

    # 하나의 제곱 수로 나타낼 수 있는 자연수라면 1을 출력하고 끝낸다.
    if dp[n] == 1:
        print(dp[n])


    else:
        for i in range(2, n + 1):
            # 완전제곱수는 로직을 돌릴 필요가 없다.
            if dp[i] == 1:
                continue
            min_cnt = n

            ## 루트까지만 진행
            for k in range(1, int(i ** .5) + 1):
                square = k ** 2
                front_idx = i - square
                rear_idx = square
                ## min 함수 쓰는 것보다 더 짧은가?
                if min_cnt > dp[front_idx] + dp[rear_idx]:
                    min_cnt = dp[front_idx] + dp[rear_idx]
                    ## 이건 나도 넣었던 부분
                    # 두 dp table 요소의 합이 2이면 더이상 확인할 필요가 없다.
                    if min_cnt == 2:
                        break
            dp[i] = min_cnt
        print(dp[n])


if __name__ == '__main__':
    solution_017626()