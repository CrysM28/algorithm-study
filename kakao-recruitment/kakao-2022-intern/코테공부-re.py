a = 0
c = 0
#p = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
p = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]



def solution(alp, cop, problems):
    INF = int(1e9)

    # 목표 알고력, 목표 코딩력
    problems.sort()
    target_alp = problems[-1][0]
    problems.sort(key=lambda x: x[1])
    target_cop = problems[-1][1]

    # 목표가 주어진 능력보다 낮을 수 있음
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)


    # 2차원 dp 배열 (dp[a][c] = 최단시간)
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    # 문제 안 풀고 공부했을때로 채우기
    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):
            # 알고력
            if a + 1 <= target_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            # 코딩력
            if c + 1 <= target_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 문제풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    next_alp, next_cop = min(target_alp, a + alp_rwd), min(
                        target_cop, c + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],
                                                 dp[a][c] + cost)

    print(*dp, sep="\n")

    # print(target_alp, target_cop)
    # print(problems)
    time = dp[-1][-1]
    return time


print(solution(a, c, p))
