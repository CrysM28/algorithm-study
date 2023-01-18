# 2467. 용액
## Python3은 148, PyPy3는 160으로 더 느림 반복이 많이 없어서 그런가?

N = int(input())
solutions = list(map(int, input().split()))

start = 0
end = N-1

ans = abs(solutions[start] + solutions[end])
ans_left = solutions[start]
ans_right = solutions[end]

while start < end:
    next_val = solutions[start] + solutions[end]

    # 용액 합 업데이트
    if ans > abs(next_val):
        ans = abs(next_val)
        ans_left = solutions[start]
        ans_right = solutions[end]
    
    # 포인터 위치 조정
    if next_val > 0:
        end -= 1
    elif next_val < 0:
        start += 1
    else:
        break


print(ans_left, ans_right)