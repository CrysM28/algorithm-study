# 11723. 집합
## pypy3로 돌리면 메모리 초과

import sys
from collections import deque

s = set()
cmd_num = int(input())

for _ in range(cmd_num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'add':
        s.add(int(cmd[1]))

    elif cmd[0] == 'remove':
        try:
            s.remove(int(cmd[1]))
        except:
            pass
        
    elif cmd[0] == 'check':
        if int(cmd[1]) in s: print(1)
        else: print(0)
    
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s: s.remove(int(cmd[1]))
        else: s.add(int(cmd[1]))
    
    elif cmd[0] == 'all':
        s = set([x for x in range(1, 21)])
    
    elif cmd[0] == 'empty':
        s = set()
