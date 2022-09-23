# 정답 보고 다시 짜기

from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    summits.sort()
    summits_set = set(summits)

    # 등산로 입력
    graph = defaultdict(list)
    for i, j, w in paths:
        # # 출입구: 나가기만 가능 / 산봉우리: 들어오기만 가능
        # if i in gates or j in summits:
        #     graph[i].append((j, w))
        # elif j in gates or i in summits:
        #     graph[j].append((i, w))
        # else:
        graph[i].append((j, w))
        graph[j].append((i, w))


    # dijkstra
    intensity = [10000001] * (n+1)

    # 모든 출입구를 넣고 시작
    unvisited = []
    for gate in gates:
        heappush(unvisited, (0, gate))
        intensity[gate] = 0

    while unvisited:
        #print(unvisited)
        cost, node = heappop(unvisited)

        if node in summits_set or intensity[node] < cost:
            continue

        for v, w in graph[node]:
            alt = max(cost, w)  # intensity: 경로에서의 최대값
            if intensity[v] > alt:
                intensity[v] = alt
                heappush(unvisited, (alt, v))

        #print(intensity)


    min_intensity = [0, 10000001]

    for summit in summits:
        if min_intensity[1] > intensity[summit]:
            min_intensity[0] = summit
            min_intensity[1] = intensity[summit]

    return min_intensity



# print(
#     solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1],
#                  [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
# print(
#     solution(
#         7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
#         [1], [2, 3, 4]))
# print(
#     solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4],
#                  [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
#print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))