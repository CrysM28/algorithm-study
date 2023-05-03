# 16940. BFS 스페셜 저지
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = list(map(int, input().split()))


def bfs():
    if answer[0] != 1:
        return False

    idx = 1
    visited = [False] * (N+1)
    visited[1] = True
    queue = deque([1])
    

    while queue:
        v = queue.popleft()
        next_queue = []

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                next_queue.append(w)
        
        cnt = len(next_queue)
        # print(next_queue)
        # print(idx, idx+cnt)

        if sorted(answer[idx:idx+cnt]) == sorted(next_queue):
            for child in answer[idx:idx+cnt]:
                queue.append(child)
            idx += cnt
        else:
            return False

    return True


if bfs():
    print(1)
else:
    print(0)

