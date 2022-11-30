# 2933. 미네랄
import copy

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


# RxC 동굴
R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]

# 막대 던진 횟수, 높이
N = int(input())
sticks = list(map(int, input().split()))



# 근처 미네랄 클러스터 확인
def find_cluster(i, j):
    global on_ground

    if i < 0 or i >= R or \
        j < 0 or j >= C or \
            grid[i][j] != 'x':
        return

    grid[i][j] = 'o'
    clusters.append((i, j))

    # 땅에 맞닿아 있으면 괜찮음
    if i == R - 1:
        on_ground = True
        return

    find_cluster(i - 1, j)
    find_cluster(i + 1, j)
    find_cluster(i, j - 1)
    find_cluster(i, j + 1)



# 떠있는 클러스터 중력 받고 떨어지게 하기
def cluster_gravity():
    # 너비순(column, j), 바닥에 가까운 순(-row, i) 정렬
    clusters.sort(key = lambda x:(x[1], -x[0]))

    # 얼마나 내릴 수 있는지 확인용 checkers
    checkers = [clusters[0]]
    max_i = clusters[0][0]
    prev_j = clusters[0][1]
    for i, j in clusters:
        if j != prev_j:
            prev_j = j
            max_i = max(max_i, i)
            checkers.append((i,j))

    # 얼마나 내릴 수 있는지 확인
    cannot_down = False
    for down in range(1, R - max_i):
        for i, j in checkers:
            if cave[i+down][j] == 'x':
                cannot_down = True
                break
        if cannot_down:
            break
    else:
        down += 1

    down -= 1
    
    # 내릴 수 있는 만큼 내리기
    for i, j in clusters:
        cave[i][j] = '.'
        cave[i+down][j] = 'x'
    


for turn in range(N):
    stick = sticks[turn]  # 이번에 던지는 막대 높이
    line = cave[-stick]  # 그 높이의 동굴


    ## 1. 깨지는 미네랄 위치
    mx, my = R - stick, -1

    # 던지기: 짝수면 왼->오, 홀수면 오->왼
    if turn % 2 == 0:
        for i in range(C):
            if line[i] == 'x':
                my = i
                break
    else:
        for i in range(C - 1, -1, -1):
            if line[i] == 'x':
                my = i
                break

    # 이번에 깨지는 미네랄 없으면 스킵
    if my == -1:
        continue
    # 미네랄 깨기
    cave[mx][my] = '.'

    # print("before", stick)
    # print(*cave, sep='\n')

    ## 2. 깨지는 미네랄 근처 클러스터 확인
    for dir in range(4):
        grid = copy.deepcopy(cave)
        clusters = []
        on_ground = True

        nx = mx + dx[dir]
        ny = my + dy[dir]

        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'x':
            on_ground = False
            find_cluster(nx, ny)

        # 땅에 맞닿아 있지 않으면 내려야함
        if not on_ground:
            cluster_gravity()
            break

    # print("after", stick)
    # print(*cave, sep='\n')

for c in cave:
    print(*c, sep="")





'''
RxC 동굴
왼->오->왼 순서로 1~R 높이로 막대를 던짐
x를 만나면 파괴되고 중력에 의해 떨어짐
근데 그 모양은 유지됨

프로세스
1. 아래서부터 높이 잼 (즉, row 세는게 반대)
    마이너스 인덱스 쓰면 될듯
2. 던지는 순서 0~N이라 치면 
    짝수면 왼->오
    홀수면 오->왼
    순서로 그 높이의 x 확인함
3. 제거되는 걸 구해서 제거

4. 제거되는 거 좌표 기준으로 상하좌우 확인
    x가 있으면 그 x가 바닥까지 (R까지) 가는지 확인
    붙어있으면 ok
    아니라면 !!한칸씩 내리는 작업 필요!!
        이걸 위해서 확인할 때 모든 좌표 저장해놓아야 함

5. 모양 확인법
    너비 (column, j)
        에서 가장 밑 부분과 가까운 곳만 저장해놓기
    그래서 x나 R을 만나기 전까지 내려보고 얼마나 내려야하는지 그 정도를 정하고
    그게 정해지면 전체 좌표에서 그만큼 i의 좌표만 +하면 옮기기 완료
    


'''