
# check 함수를 그냥 반복문으로 돌려서 따로 만들어 놓는 게 깔끔하긴 한듯
def check(N, h, w):
    num = arr[h][w]
    for i in range(h, h+N):
        for j in range(w, w+N):
            if arr[i][j] != num:
                return False

    return True

def compact(N, h, w):
    num = arr[h][w]
    if check(N, h, w):
        print(num, end='')
        return

    print('(', end='')
    compact(N//2, h, w)
    compact(N//2, h, w+N//2)
    compact(N//2, h+N//2, w)
    compact(N//2, h+N//2, w+N//2)
    print(')', end='')


N = int(input())

arr = [list(input()) for _ in range(N)]
# print(*arr, sep='\n')
compact(N, 0, 0)