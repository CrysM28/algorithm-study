# 15684. 사다리 조작
import copy

def test():
    for n in range(N):
        cur_ladder = n

        for h in range(H):
            if cur_ladder > 0 and ladders[h][cur_ladder-1] == 1:
                cur_ladder -= 1
            elif ladders[h][cur_ladder] == 1:
                cur_ladder += 1

        
        #print(n, cur_ladder)
        if cur_ladder != n:
            return False

    return True


def add_ladder(num, init_i):
    global ans

    # elif cnt == 3 or ans <= cnt:
    if num == 4:
        return

    if test():
        # print("==", num)
        # print(*ladders, sep='\n')
        ans = min(ans, num)
        return


    for i in range(init_i, H):
        for j in range(N-1):
            # 사다리 놓일 곳 확인
            if ladders[i][j] == 0 and ladders[i][j+1] == 0:
                if j == 0 or ladders[i][j-1] == 0:
                    ladders[i][j] = 1
                    add_ladder(num+1, i)
                    ladders[i][j] = 0




N, M, H = map(int, input().split())

# 1 -> i+1과 연결
ladders = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladders[a-1][b-1] = 1


ans = 4

add_ladder(0, 0)

if ans == 4:
    ans = -1

print(ans)

# print(ans if ans < 4 else -1)