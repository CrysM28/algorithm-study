# 10:05 ~ 12:00 인데 못 풀었어... 코테 떨어지겠군 ㅋㅋ ㅠ

from collections import defaultdict, deque
import heapq as h

def bfs(graph, gates, summits, start, target):
    visited = [start]
    q = [(0,start)]
    intensity = 0

    while q:
        w,v = h.heappop(q)

        # 출발지, 목적지 이외의 출입구, 정상은 방문 X
        if (v != start and v in gates) or (v != target and v in summits):
            continue

        # 거리 짧은 순으로 스택에 넣기
        for node, time in graph[v]:
            print(v, node, time)
            if node not in visited:
                h.heappush(q, (time,node))
                visited.append(node)
                intensity = max(intensity, w)

            # 정상에 도달했으면 intensity 최소값 비교
            if v == target:
                print("im summit", v)
                break



    print(visited)
    return [v, intensity]


def solution(n, paths, gates, summits):
    # 등산로
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    for a in graph:
        graph[a].sort()

    min_path = [int(1e9), int(1e9)]
    for g in gates:
        print("g going", g)
        for s in summits:
            res = bfs(graph, gates, summits, g, s)
            print("==result", g, s, res)
            if min_path[1] > res[1]:
                min_path = res

    return min_path


# print(
#     solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1],
#                  [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(
    solution(
        7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
        [1], [2, 3, 4]))
# print(
#     solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4],
#                  [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
