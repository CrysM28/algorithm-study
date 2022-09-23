# 정답 보고 다시 짜기

from collections import defaultdict, deque
from heapq import heappop, heappush




def solution(n, paths, gates, summits):
    answer = []

    # 등산로 입력
    graph = defaultdict(list)
    for i, j, w in paths:
        # 출입구: 나가기만 가능
        if i in gates:
            graph[i].append((j, w))
        # 산봉우리: 들어오기만 가능
        elif i in summits:
            graph[j].append((i, w))
        else:
            graph[i].append((j, w))
            graph[j].append((i, w))


    print(graph)

    def dijkstra(start):
        dist = defaultdict(int)
        unvisited = [(0, start)]  # (time, node)

        while unvisited:
            time, node = heappop(unvisited)

            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heappush(unvisited, (alt, v))

        return dist



    dijkstra()



    return answer


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
