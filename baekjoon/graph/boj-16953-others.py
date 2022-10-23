A, B = map(int,input().split(' '))

# idea -> 반대로 접근. B를 2로 나눌 수 있을 만큼 나누다가
# 2로 나누어서 나머지가 생기는 경우라면 1을 빼주고
count = 1
# 홀수는 1을 제외하고는 나올 수 없음. 예외처리

while True:

    if B == A:
        break

    elif B % 2 == 1 and B % 10 != 1:
        count = -1
        break

    elif B == 0:
        count = -1
        break

    count += 1
    surplus = B % 2
    if surplus == 1:
        B = B // 10
    else:
        B = int(B / 2)

print(count)