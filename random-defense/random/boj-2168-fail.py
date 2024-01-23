# 2168. 타일 위의 대각선
## 인터넷 풀이 참고..

X, Y = map(int, input().split())
if X > Y:
    X, Y = Y, X




















def my_solution1(x, y):
    total = 0
    if x == 1:
        return y

    nx = x // 2
    ny = y // 2

    # 홀수가 있을 때
    if x % 2 != 0 or y % 2 != 0:
        total += (y // x + 1) * x
    else:
        total += recursive(nx, ny) * 2
    
    return total


