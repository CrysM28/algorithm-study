# 3:45~ 5:15 (1시간 30분..)

info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8],
          [6, 9], [9, 10]]

from collections import defaultdict


def solution(info, edges):

    SHEEP = 0
    WOLF = 1

    def count(x):
        sheep = 0
        wolf = 0

        if which[x] == SHEEP:
            sheep += 1
        elif which[x] == WOLF:
            wolf += 1

        if parent[x] != x:
            s, w = count(parent[x])
            sheep += s
            wolf += w

        return sheep, wolf

    # 부모 초기화
    parent = [i for i in range(len(info))]

    # 양, 늑대 연결 정보
    which = dict()  # 노드에 있는 게 무엇인지
    for idx, i in enumerate(info):
        which[idx] = i

    # 그래프 형태
    graph = defaultdict(list)
    for e in edges:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
        parent[b] = a

    print("graph")
    print(graph)

    print(parent)

    animals = defaultdict(list)

    for i in range(len(info)):
        animals[i] = count(i)

    print(animals)

    answer = 0

    return answer


print(solution(info1, edges1))