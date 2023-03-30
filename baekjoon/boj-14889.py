# 14889. 스타트와 링크

# 답: 최소 능력치 차이
ans = int(1e9)

def make_team(depth, idx):
    global ans

    if depth == N//2:
        # 나머지 팀 꾸리기
        team_link = [i for i in range(N) if not is_team_start[i]]
                
        # 시너지 계산
        team_start_power, team_link_power = 0, 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                s1, s2 = team_start[i], team_start[j]
                l1, l2 = team_link[i], team_link[j]
                team_start_power += power[s1][s2] + power[s2][s1]
                team_link_power += power[l1][l2] + power[l2][l1]

        # 이게 시간이 더 많이 걸림
        # team_start_power, team_link_power = 0, 0
        # for i in range(N):
        #     for j in range(i, N):
        #         if is_team_start[i] and is_team_start[j]:
        #             team_start_power += power[i][j] + power[j][i]
        #         elif not is_team_start[i] and not is_team_start[j]:
        #             team_link_power += power[i][j] + power[j][i]

        # 차이 최소값 저장
        power_diff = abs(team_start_power - team_link_power)
        ans = min(ans, power_diff)

        return

    # 팀 만들기
    for person in range(idx, N):
        if not is_team_start[person]:
            team_start.append(person)
            is_team_start[person] = True
            make_team(depth+1, person+1)
            is_team_start[person] = False
            team_start.pop()



N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]

is_team_start = [False] * N
team_start = []
checked = set()

make_team(0, 0)

print(ans)