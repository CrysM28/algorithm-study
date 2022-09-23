# 9:00 ~

a = 0
c = 0
#p=[[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
p = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]


def solution(alp, cop, problems):
    time = 0

    # 모든 문제 풀기 위한 알고력, 코딩력
    problems.sort(key=lambda x: (x[0], x[1]))
    target_alp = problems[-1][0]
    target_cop = problems[-1][1]

    # 시간이 가장 적게 들고, 요구 적은 순, 많이 올려주는 순으로 정렬
    # 알고력보다 코딩력이 더 많이 필요하면 코딩력을 더 많이 주는 것부터
    if target_alp < target_cop:
        problems.sort(key=lambda x: (x[4], x[0], x[1], -x[3], -x[2]))
    else:
        problems.sort(key=lambda x: (x[4], x[0], x[1], -x[2], -x[3]))

    print(target_alp, target_cop)
    print(problems)



    while True:
        # 종료 조건
        if alp >= target_alp and cop >= target_cop:
            break

        # 현재 푸는 문제 번호
        n = 0

        
        # 다음 문제 푸는데 필요한 알고력, 코딩력
        next_alp = problems[n+1][0]
        next_cop = problems[n+1][1]

        # 을 채울때까지 문제풀기 
        time1 = next_alp // problems[n][0]
        time2 = next_cop // problems[n][1]

        
        if time1 < time2:


        # 문제 푸는것보다 생공부가 덜 걸리면 생공부하기



        # 조건 채웠으면 다음 문제로 옮겨가고, 다음 목표 재설정




        # 
        #while alp > problems[n][0] and cop > problems[n][1]:

            








    # # 알고력
    # if alp < p[0]:
    #     time += p[0] - alp

    # # 코딩력
    # if cop < p[1]:
    #     time += p[1] - cop

    # alp += p[2]
    # cop += p[3]
    # time += p[4]

    # print(p, alp, cop, time)

    return time


print(solution(a, c, p))
