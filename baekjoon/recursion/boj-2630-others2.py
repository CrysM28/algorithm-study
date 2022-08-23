import sys

input = sys.stdin.readline

blue = 0
white = 0


def search(x, y, n):
    global blue
    global white

    s = sum([sum(i[y:y + n]) for i in l[x:x + n]])
    if s == n * n:
        blue += 1
        return
    if s == 0:
        white += 1
        return
    if s != n * n or s != 0:
        search(x, y, n // 2)
        search(x, y + n // 2, n // 2)
        search(x + n // 2, y, n // 2)
        search(x + n // 2, y + n // 2, n // 2)
        return


N = int(input())
l = [list(map(int, input().split())) for i in range(N)]

search(0, 0, N)
print(white)
print(blue)