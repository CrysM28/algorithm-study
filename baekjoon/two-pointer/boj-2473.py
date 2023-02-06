# 2473. 세 용액
INF = int(1e10)

N = int(input())
sol = sorted(list(map(int, input().split())))

ans = [INF] * 3
ans_sum = INF

# 하나 고정하고 나머지 투포인터 탐색
for i in range(N-2):
    start = i+1
    end = N-1

    while start < end:
        next_val = sol[i] + sol[start] + sol[end]

        # 최소값 찾았으면 바로 끝내기
        if next_val == 0:
            ans = [sol[i], sol[start], sol[end]]
            break

        # 용액 합 업데이트
        if ans_sum > abs(next_val):
            ans = [sol[i], sol[start], sol[end]]
            ans_sum = abs(next_val)
        
        # 포인터 위치 조정
        if next_val > 0:
            end -= 1
        elif next_val < 0:
            start += 1
        else:
            break

print(*ans)
