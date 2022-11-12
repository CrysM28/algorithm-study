# 16974. 레벨 햄버거

# 레벨-N 버거, X장
N, X = map(int, input().split())

# [i][0]: size, [i][1]: patty
burger = [[0]*2 for _ in range(N+1)]
burger[0][0] = 1
burger[0][1] = 1

for i in range(1, N+1):
    burger[i][0] = burger[i-1][0]*2 + 3
    burger[i][1] = burger[i-1][1]*2 + 1



def find_patty(level, pos):    
    half = burger[level][0] // 2

    # level 0 버거는 무조건 패티
    if level == 0:
        return 1

    # 맨 왼쪽: 무조건 번    
    if pos == 0:
        return 0
    # 맨 오른쪽: 전부
    elif pos == burger[level][0]:
        return burger[level][1]
    # 중간
    elif pos == half:
        return 1 + burger[level-1][1]
    # 오른쪽
    elif pos > half:
        new_pos = pos - burger[level-1][0] - 2
        return find_patty(level-1, new_pos) + 1 + burger[level-1][1]
    # 왼쪽
    else:
        new_pos = pos - 1
        return find_patty(level-1, new_pos)


ans = find_patty(N, X-1)
print(ans)



'''
레벨 L 버거

번
L-1 버거
패티
L-1버거
번

어차피 대칭이니까 굳이 뒤에서부터 먹을 필요도 없고
앞에서부터 카운트해도 되네;
'''