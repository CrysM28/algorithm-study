# 1074. Z
## 1,2,3,4분면 구분 (좌표평면 X, Z모양 기준)

def find_point(i, j, n, cur_lu):
    lu = cur_lu  # left-uppermost number

    # Z 모양 탐색
    if n == 1:
        lu += i*2 + j
        return lu

    # 사분면 판별
    row = i // 2**(n - 1)
    col = j // 2**(n - 1)

    # left-up
    if row == 0 and col == 0:
        lu += 0
        row = i
        col = j

    # right-up
    elif row == 0 and col == 1:
        lu += 2**(2 * (n - 1)) * 1
        row = i
        col = j-2**(n - 1)

    # left-down
    elif row == 1 and col == 0:
        lu += 2**(2 * (n - 1)) * 2
        row = i-2**(n - 1)
        col = j

    # right-down
    elif row == 1 and col == 1:
        lu += 2**(2 * (n - 1)) * 3
        row = i-2**(n - 1)
        col = j-2**(n - 1)

    lu = find_point(row, col, n - 1, lu)
    return lu

N, r, c = map(int, input().split())
ans = find_point(r, c, N, 0)
print(ans)
