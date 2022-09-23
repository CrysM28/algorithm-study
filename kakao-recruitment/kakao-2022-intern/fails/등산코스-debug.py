# 10:05 ~
from collections import defaultdict


def dfs(graph, gates, summits, start, summit):
    visited = []
    stack = [(start,0)]
    intensity = 0

    print("--start==")
    while stack:
        print("stack", stack)
        print("visited", visited)

        v, w = stack.pop()
        print("v,w",v,w)

        # 출발점 의외의 출입구, 목적점 이외의 정상은 거치지 않음
        if (v != start and v in gates) or (v != summit and v in summits):
            print("sth ", v)
            continue

        if v not in visited:
            visited.append(v)
            intensity = max(intensity, w)

            # 정상에 도달했으면 끝
            if v == summit:
                print("im summit", v)
                break

            tmp = graph[v][:]
            print(graph)
            print("인접", tmp)
            while tmp:
                stack.append(tmp.pop())

    print("end", visited)

    return [intensity, summit]


def solution(n, paths, gates, summits):
    # 등산로
    graph = defaultdict(list)
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    for a in graph:
        graph[a].sort()


    min_path = [int(1e10)]
    for g in gates:
        for s in summits:
            result = dfs(graph, gates, summits, g, s)
            print("result==", g, s, result)
            # intensity 최소값
            if min_path[0] > result[0]:
                min_path = result

            print(min_path)

    answer = []
    # 포함 summits
    # for s in summits:
    #     if s in min_path[1]:
    #         answer.append(s)
    #         break
    # # intensity
    # answer.append(min_path[0])

    return answer





print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
#print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))