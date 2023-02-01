# 11729. 하노이 탑 이동 순서

def hanoi(n, from_pos, to_pos, tmp_pos):
    global cnt

    if n == 1:
        cnt += 1
        #print(from_pos, to_pos)
        answer.append([from_pos, to_pos])
        return

    # 가장 큰 거 제외 남는 기둥에 옮기기
    hanoi(n-1, from_pos, tmp_pos, to_pos)

    # 가장 큰 거 하나 옮기기
    #print(from_pos, to_pos)
    answer.append([from_pos, to_pos])
    cnt += 1
    
    # 남는 기둥에 있는 거 가장 큰 거 위로 옮기기
    hanoi(n-1, tmp_pos, to_pos, from_pos)


N = int(input())

answer = []
cnt = 0

hanoi(N, 1, 3, 2)

print(cnt)
for a in answer:
    print(*a)
