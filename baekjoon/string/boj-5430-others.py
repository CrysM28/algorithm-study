import sys
from collections import deque

a = int(sys.stdin.readline().rstrip())
for i in range(a):
    ac = list(sys.stdin.readline().rstrip())
    num = int(sys.stdin.readline().rstrip())
    d = ac.count('D')

    arr = sys.stdin.readline().rstrip()

    # 일일이 해보지 말고 처음부터 d가 많으면 넘기기
    if d > num:
        print('error')
        continue
    
    arr = arr.strip('[]').split(',')
    arr1 = deque([i for i in arr if i != ''])
    cnt = 0
    for i in ac:
        if i == 'R':
            cnt += 1
        else:
            if cnt % 2 == 0:
                arr1.popleft()
            else:
                arr1.pop()

    print('[',
          ','.join((list(arr1) if cnt % 2 == 0 else list(arr1)[::-1])),
          ']',
          sep='')
