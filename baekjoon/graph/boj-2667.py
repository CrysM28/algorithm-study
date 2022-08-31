# 2667. 단지번호붙이기
## 딱 봐도 dfs/bfs 탐색 문제
n = int(input())
map = [list(input()) for _ in range(n)]

home = []  # 단지별 주택 수 저장
home_no = 0  # 단지 번호
home_num = 0  # 단지 개수


def dfs(i, j):
    num = 0

    # 범위 밖이거나 아직 체크 안 한 집이 아니면 X
    if i < 0 or i >= n or j < 0 or j >= n or map[i][j] != '1':
        return 0

    # 범위 안이고 집이 있는 곳이면 체크 후 방문표시, 집 발견 +1
    map[i][j] = home_no
    num += 1

    # 앞뒤좌우 확인
    num += dfs(i - 1, j)
    num += dfs(i + 1, j)
    num += dfs(i, j - 1)
    num += dfs(i, j + 1)

    # 현 단지의 총 집 개수
    return num


for i in range(n):
    for j in range(n):
        # 하나의 단지 찾기 
        home_num = dfs(i, j)

        # 집이 하나라도 있었으면 단지; 정보 저장
        if home_num > 0:
            home.append(home_num)
            home_no += 1


# 총 단지 수
print(home_no)

# 단지내 집 수 (오름차순)
home.sort()
print(*home, sep="\n")
