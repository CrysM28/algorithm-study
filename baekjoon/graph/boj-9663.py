# 9663. N-Queen

def nqueen(i):
    global count

    # N개의 퀸을 다 놓았으면 +1
    if i == N:
        count += 1
        return

    for j in range(N):
        # 수직 확인
        if j not in queens:
            # 대각선 확인
            is_diag = False
            for x, y in enumerate(queens):
                if abs(i - x) == abs(j - y):
                    is_diag = True
                    break

            if not is_diag:
                queens.append(j)
                nqueen(i + 1)
                queens.pop()


N = int(input())

queens = []  # 퀸 좌표: (i,j) -> queens[i] = j
count = 0

nqueen(0)

print(count)
