# 1992. 쿼드트리

def cut(start_i, start_j, length):
    # 나눈 영역
    cur_arr = [
        row[start_j:start_j + length]
        for row in arr[start_i:start_i + length]
    ]

    # 종료 조건: 모두 같은 수
    same_0, same_1 = True, True
    for p in cur_arr:
        if same_0 and all(pp == 0 for pp in p):
            same_1 = False
        elif same_1 and all(pp == 1 for pp in p):
            same_0 = False
        else:
            break
    else:
        if same_0:
            quadtree.append('0')
            return
        elif same_1:
            quadtree.append('1')
            return

    # 더 쪼개기
    cur_len = length // 2

    quadtree.append('(')
    for i in range(0, length, cur_len):
        for j in range(0, length, cur_len):
            cut(start_i + i, start_j + j, cur_len)
    quadtree.append(')')


N = int(input())
arr = []
quadtree = []

for _ in range(N):
    arr.append(list(map(int, input())))

cut(0,0,N)

print(''.join(quadtree))