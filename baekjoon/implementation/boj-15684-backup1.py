# 15684. 사다리 조작
import copy

def test():
    for n in range(N):
        cur_ladder = n
        #print(n)
        for h in range(H):
            if ladders[h][cur_ladder] == 1:
                if cur_ladder-1 >= 0 and ladders[h][cur_ladder-1] == 1:
                    cur_ladder -= 1
                elif cur_ladder+1 < N and ladders[h][cur_ladder+1] == 1:
                    cur_ladder += 1
            #print(h, cur_ladder)
        
        print(n, cur_ladder)
        if cur_ladder != n:
            return False

    return True


def add_ladder(num, init_i):
    global ans

    if num == 4:
        return

    for i in range(init_i, H):
        for j in range(N):
            # 사다리 놓일 곳 확인
            if j+1<N and ladders[i][j] == 0 and ladders[i][j+1] == 0:
                # 양옆 확인
                if (j-1<0 or ladders[i][j-1] == 0) and (j+2>=N or ladders[i][j+2] == 0):                    
                    ladders[i][j] = 1
                    ladders[i][j+1] = 1

                    #print("- before test")
                    print("==", num)
                    print(*ladders, sep='\n')

                    if test():
                        print("yes")
                        ans = min(ans, num)
                        return

                    add_ladder(num+1, i)

                    ladders[i][j] = 0
                    ladders[i][j+1] = 0




N, M, H = map(int, input().split())

ladders = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladders[a-1][b-1] = 1
    ladders[a-1][b] = 1


print(*ladders, sep='\n')

ans = 4

if test():
    ans = 0
else:
    add_ladder(1, 0)

if ans == 4:
    ans = -1


print(ans)