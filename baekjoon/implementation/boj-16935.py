# 16935. 배열 돌리기 3

# N, M 확인
def check_NM(array):
    n = len(array)
    m = len(array[0])
    return n, m

# 상하반전
def ops1():
    for j in range(M):
        for i in range(N//2):
            arr[i][j], arr[-(i+1)][j] = arr[-(i+1)][j], arr[i][j]

# 좌우반전
def ops2():
    for i in range(N):
        for j in range(M//2):
            arr[i][j], arr[i][-(j+1)] = arr[i][-(j+1)], arr[i][j]

# 오른쪽 90도
def ops3():
    new_arr = []
    for j in range(M):
        tmp = []
        for i in range(1, N+1):
            tmp.append(arr[-i][j])
        new_arr.append(tmp)    
    return new_arr

# 왼쪽 90도
def ops4():
    new_arr = []
    for j in range(1, M+1):
        tmp = []
        for i in range(N):
            tmp.append(arr[i][-j])
        new_arr.append(tmp)
    return new_arr


# 사분면 시계방향 회전
def ops5():
    new_arr = []

    for i in range(N//2):
        # 4
        tmp = arr[N//2 + i][:M//2]
        # 1
        tmp += arr[i][:M//2]

        new_arr.append(tmp)
    
    for i in range(N//2):
        # 3
        tmp = arr[N//2 + i][M//2:]
        # 2
        tmp += arr[i][M//2:]
        
        new_arr.append(tmp)

    return new_arr


# 사분면 반시계방향 회전
def ops6():
    new_arr = []

    for i in range(N//2):
        # 2
        tmp = (arr[i][M//2:])
        # 3
        tmp += arr[N//2 + i][M//2:]
        new_arr.append(tmp)
    
    for i in range(N//2):
        # 1
        tmp = (arr[i][:M//2])
        # 4
        tmp += arr[N//2 + i][:M//2]
        new_arr.append(tmp)
    
    return new_arr

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))


for ops in operations:
    N, M = check_NM(arr)

    if ops == 1:
        ops1()
    elif ops == 2:
        ops2()
    elif ops == 3:
        arr = ops3()
    elif ops == 4:
        arr = ops4()
    elif ops == 5:
        arr = ops5()
    elif ops == 6:
        arr = ops6()



for rows in arr:
    print(*rows)
