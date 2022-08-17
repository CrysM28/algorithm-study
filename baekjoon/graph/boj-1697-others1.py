# Python3 - 208 ms

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())


def bfs(n):
    queue = deque()
    queue.append([n, 0])
    visited = [0] * 200001      # index 사용해서 탐색 O(1)으로
    visited[n] = 1
    while queue:
        u, cnt = queue.popleft()
        if u == k:
            print(cnt)
            break
        # 큐에 넣을 때 몇초대의 숫자인지를 같이 넣어줌
        else:
            # -1: 음수 아닐때
            if u - 1 >= 0 and visited[u - 1] == 0:
                queue.append([u - 1, cnt + 1])
                visited[u - 1] = 1

            # +1: n, k보다 작을 때
            if u + 1 <= max(n, k) and visited[u + 1] == 0:
                queue.append([u + 1, cnt + 1])
                visited[u + 1] = 1
                
            # *2: k보다 작을 때
            if 0 < u < k and visited[2 * u] == 0:
                queue.append([2 * u, cnt + 1])
                visited[2 * u] = 1


bfs(n)