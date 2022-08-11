# 10866. 덱

import sys
from collections import deque

queue = deque()
cmd_num = int(input())

for _ in range(cmd_num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        queue.append(int(cmd[1]))

    elif cmd[0] == 'pop_front':
        if not queue: print("-1")
        else: print(queue.popleft())
    elif cmd[0] == 'pop_back':
        if not queue: print("-1")
        else: print(queue.pop())

    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if not queue: print("1")
        else: print("0")
    elif cmd[0] == 'front':
        if not queue: print("-1")
        else: print(queue[0])
    elif cmd[0] == 'back':
        if not queue: print("-1")
        else: print(queue[-1])
