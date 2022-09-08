# 1780. 종이의 개수


def cut(start_i, start_j, length):
    # 총 종이 개수
    num_minus, num_0, num_1 = 0, 0, 0

    # 자른 종이
    cur_paper = [
        row[start_j:start_j + length]
        for row in paper[start_i:start_i + length]
    ]

    # 종료 조건 1: 종이의 크기가 1
    if length == 1:
        if cur_paper[0][0] == -1:
            return 1, 0, 0
        elif cur_paper[0][0] == 0:
            return 0, 1, 0
        elif cur_paper[0][0] == 1:
            return 0, 0, 1

    # 종료 조건 2: 종이가 모두 같은 수
    same_minus, same_0, same_1 = True, True, True
    for p in cur_paper:
        if same_minus and all(pp == -1 for pp in p):
            same_0, same_1 = False, False
        elif same_0 and all(pp == 0 for pp in p):
            same_minus, same_1 = False, False
        elif same_1 and all(pp == 1 for pp in p):
            same_minus, same_0 = False, False
        else:
            break
    else:
        if same_minus:
            return 1, 0, 0
        elif same_0:
            return 0, 1, 0
        elif same_1:
            return 0, 0, 1

    # 더 쪼개기
    cur_len = length // 3
    for i in range(0, length, cur_len):
        for j in range(0, length, cur_len):
            total_num = cut(start_i + i, start_j + j, cur_len)
            num_minus += total_num[0]
            num_0 += total_num[1]
            num_1 += total_num[2]

    return num_minus, num_0, num_1


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

ans = cut(0, 0, N)
for a in ans:
    print(a)
