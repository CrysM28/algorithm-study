# 1072. 게임
MAX = int(1e9)
x, y = map(int, input().split())
z = y * 100 // x
print(z)

start, end = 0, MAX
answer = 0

# 매개변수 탐색
while start <= end:
    mid = (start + end) // 2
    new_z = int((y + mid) / (x + mid) * 100)
    print("new", start, end, mid, new_z)

    if new_z > z:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

if answer == 0:
    print(-1)
else:
    print(answer)
