# Python3 - 152 ms

from collections import deque

def bfs():
  qq = deque()
  qq.append(a)

  while qq:
    v = qq.popleft()

    if v == b:
      print(line[v])
      break

    for i in (v-1,v+1,v*2):
      if 0 <= i <= upper and not line[i]:
        line[i] = line[v] + 1
        qq.append(i)
a,b = map(int,input().split())

upper = 10 ** 5     # upper-bound를 100,000으로 잡음 -> 문제에 있는 조건임

line = [0] *(upper+1)

bfs()
