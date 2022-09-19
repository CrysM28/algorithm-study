# 왕실의 나이트
## 풀이 참고

# 나이트 현재 위치
a = input()
row = int(a[1])
col = int(ord(a[0]) - ord('a')) + 1

# 나이트가 이동할 수 있는 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동가능한지 확인
move = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1<= next_col <= 8:
        move += 1
        
print(move)