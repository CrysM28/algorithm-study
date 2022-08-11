# 10845. 큐
## 큐 연산 구현하는 문제

import sys
from collections import deque

queue = deque()
cmd_num = int(input())  # 주어지는 명령의 수

for _ in range(cmd_num):
    cmd = sys.stdin.readline().rstrip()

    if cmd == 'pop':
        if len(queue) == 0: print("-1")
        else: print(queue.popleft())
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if not queue: print("1")
        else: print("0")
    elif cmd == 'front':
        if not queue: print("-1")
        else: print(queue[0])
    elif cmd == 'back':
        if not queue: print("-1")
        else: print(queue[-1])

    # push 처리 (다른 명령 없다는 전제 있음)
    else:
        tmp, push_num = cmd.split()
        queue.append(push_num)
