# dp 풀이 - dp 쓰는거 말고 조합론 생각하는 점에선 비슷한 풀이인듯

import sys
rdln = sys.stdin.readline

def go(idx, r, g, b):
    if r < 0 or g < 0 or b < 0:
        return 0
    if idx == 0:
        return 1
    if d[idx][r][g][b] != -1:
        return d[idx][r][g][b]
    
    d[idx][r][g][b] = 0
    # ans = d[idx][r][g][b]

    d[idx][r][g][b] += go(idx-1, r-idx, g, b)
    d[idx][r][g][b] += go(idx-1, r, g-idx, b)
    d[idx][r][g][b] += go(idx-1, r, g, b-idx)
    
    if idx % 2 == 0:
        d[idx][r][g][b] += go(idx-1,r-(idx//2),g-(idx//2),b) *c[idx][idx//2]
        d[idx][r][g][b] += go(idx-1, r-idx//2, g, b-idx//2) *c[idx][idx//2]
        d[idx][r][g][b] += go(idx-1, r, g-idx//2, b-idx//2) *c[idx][idx//2]
    
    if idx % 3 == 0:
        d[idx][r][g][b] += go(idx-1, r-idx//3, g-idx//3, b-idx//3) * c[idx][idx//3] * c[idx-idx//3][idx//3]

    return d[idx][r][g][b]

n, red, green, blue = map(int, rdln().split())
d = [[[[-1] * (101) for _ in range(101)] for _ in range(101)] for _ in range(11)]

c = [[0] * 11 for _ in range(11)]
c[0][0] = 1
for i in range(1, 11):
    c[i][0] = c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i-1][j-1] + c[i-1][j]

sys.stdout.write(f"{go(n, red, green, blue)}\n")