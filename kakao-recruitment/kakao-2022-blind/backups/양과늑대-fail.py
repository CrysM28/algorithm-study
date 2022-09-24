# 3:45~ 5:15 (1시간 30분..)

info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8],
          [6, 9], [9, 10]]

from collections import defaultdict

SHEEP = 0
WOLF = 1

max_sheep = 0


def solution(info, edges):

    def dfs(node, sheep, wolf, can_visit, visited):
        global max_sheep

        print("=== new dfs===", node)

        # 갈 수 있는 곳인지 확인
        if node not in can_visit:
            print("cannot visit", node, can_visit)
            return
        can_visit.remove(node)

        # 양, 늑대 세기
        if which[node] == SHEEP:
            sheep += 1
            max_sheep = max(max_sheep, sheep)
        elif which[node] == WOLF:
            wolf += 1

        print("sheep wolf max", sheep, wolf, max_sheep)

        # 넘어서면 돌아가기
        if sheep <= wolf:
            return

        print("visited", visited)
        print("can visit", can_visit)
        # 인접 노드 확인
        for v in graph[node]:
            if v not in visited:
                can_visit.add(v)
                visited.append(v)

                dfs(v, sheep, wolf, can_visit, visited)


        # print("node popped:", node, can_visit)

        # if which[node] == SHEEP:
        #     sheep += 1
        # elif which[node] == WOLF:
        #     wolf += 1

        # print("sheep wolf", sheep, wolf)

        # # 더 이상 탐색 진행 못하면 삭제
        # if sheep != 0 and sheep <= wolf:
        #     print("왕!", node, sheep, wolf)
        #     for v in graph[node]:
        #         if v in can_visit:
        #             can_visit.remove(v)

        #     # 지금 더한만큼 걸 뺌
        #     if which[node] == SHEEP:
        #         sheep -= 1
        #     elif which[node] == WOLF:
        #         wolf -= 1

        #     return can_visit, sheep, wolf

        # for v in graph[node]:
        #     if v in can_visit:
        #         can_visit.remove(v)
        #         can_visit, s, w = dfs(v, sheep, wolf, can_visit)
        #         print("after back", v, s, w)
        #         sheep = s
        #         wolf = w

        # return can_visit, sheep, wolf

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

    print(graph)

    dfs(0, 0, 0, {0}, [0])

    answer = 0
    return answer


print(solution(info1, edges1))