# 1406. 에디터
import sys
from collections import deque

input = sys.stdin.readline

stack = list(input().rstrip())
M = int(input())

left = stack
right = deque([])

for i in range(M):
    cmd = input()
    
    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])


    print(left, right)        

    #print(cursor)
ans = ''.join(left)
ans += ''.join(list(right))
print(ans)