# 정답 보고 다시 짜기
## 테스트케이스 일부 실패

from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    summits.sort()

    # 등산로 입력
    graph = defaultdict(list)
    for i, j, w in paths:
        # 출입구: 나가기만 가능 / 산봉우리: 들어오기만 가능
        if i in gates or j in summits:
            graph[i].append((j, w))
        elif j in gates or i in summits:
            graph[j].append((i, w))
        else:
            graph[i].append((j, w))
            graph[j].append((i, w))

    # dijkstra
    intensity = defaultdict(int)

    # 모든 출입구를 넣고 시작
    unvisited = []
    for gate in gates:
        heappush(unvisited, (0, gate))

    while unvisited:
        #print(unvisited)
        cost, node = heappop(unvisited)

        # 최소 경로만 고려
        if node not in intensity:
            intensity[node] = cost
            for v, w in graph[node]:
                alt = max(cost, w)  # intensity: 경로에서의 최대값
                heappush(unvisited, (alt, v))

        #print(intensity)


    min_no = int(1e9)
    min_int = int(1e9)

    for summit in summits:
        if min_int > intensity[summit]:
            min_no = summit
            min_int = intensity[summit]

    return [min_no, min_int]



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
#print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))