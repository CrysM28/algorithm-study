# 14502. 연구소
from collections import deque
import copy

# 상수
BLANK = 0
WALL = 1
VIRUS = 2

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

N, M = map(int, input().split())
grid = []

# 좌표 저장
viruses = []
blanks = []

# 원래 빈 칸 개수 (새로 세우는 3개의 벽만큼 제외)
org_blank = -3
# (답) 안전영역 최대 크기
max_safe = 0

for i in range(N):
    data = list(map(int, input().split()))

    for j in range(M):
        if data[j] == VIRUS:
            viruses.append((i, j))
        elif data[j] == BLANK:
            blanks.append((i, j))
            org_blank += 1

    grid.append(data)


def bfs(new_grid):
    cur_blank = org_blank
    queue = deque(viruses)

    while queue:
        #print(queue)
        x, y = queue.popleft()
        #print(x, y)

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < M and new_grid[nx][ny] == BLANK:
                queue.append((nx, ny))
                new_grid[nx][ny] = 2
                cur_blank -= 1
    
    return cur_blank

idx = []
def make_walls():
    global max_safe

    if len(idx) == 3:
        tmp = copy.deepcopy(grid)
        #print(idx)
        for i in idx:
            x, y = blanks[i]
            tmp[x][y] = 1
        
        #print(*tmp, sep='\n')

        cur_blank = bfs(tmp)
        #print(cur_blank)
        max_safe = max(cur_blank, max_safe)
        return
    
    for i in range(len(blanks)):
        if i not in idx:
            idx.append(i)
            make_walls()
            idx.pop()




#bfs()
#print(*tmp, sep='\n')
#print(cur_blank)
#print(*grid, sep='\n')
#print(viruses)
#print(blanks)
make_walls()
print(max_safe)



