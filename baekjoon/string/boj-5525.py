# 5525. IOIOI
from collections import defaultdict

n = int(input())
m = int(input())
s = input()

i = 0
cnt = 0     # IOI 반복 횟수
total = 0

while i < m-1:
    # IOI면 idx 2개 이동
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1

        # pn 완성
        if cnt == n:
            total += 1
            cnt -= 1    # 완성된 앞에 2개 빼고 다시 계속 서치

    # 다른 글자면 세던거 초기화, 다음 idx부터 다시 보기(1개만 이동)
    else:
        i += 1
        cnt = 0

print(total)