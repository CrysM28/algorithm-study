# 2630. 색종이 만들기
## 하양: 0, 파랑: 1

from collections import Counter

def divide(start_i, end_i, start_j, end_j):
    cnt = ""  # 색종이 수
    n = (end_i - start_i)  # 현재 한 변의 크기

    p = [row[start_j:end_j] for row in paper[start_i:end_i]]  # 2차원 배열 슬라이싱
    p_sum = sum([sum(i) for i in p])  # 2차원 배열 합 구하기

    # print("====", n)
    # print((start_i, end_i, start_j, end_j))
    # print(*p, sep='\n')
    # print(p_sum)

    # 모두 하양
    if p_sum == 0:
        return 'w'

    # 모두 파랑
    if p_sum == n**2:
        return 'b'

    # 색 다르면 더 나누기
    n = n // 2
    cnt += divide(start_i, start_i + n, start_j, start_j + n)  # 왼쪽 위
    cnt += divide(start_i, start_i + n, start_j + n, end_j)  # 오른쪽 위
    cnt += divide(start_i + n, end_i, start_j, start_j + n)  # 왼쪽 아래
    cnt += divide(start_i + n, end_i, start_j + n, end_j)  # 오른쪽 아래

    return cnt


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

total = Counter(divide(0, N, 0, N))
print(total['w'])
print(total['b'])