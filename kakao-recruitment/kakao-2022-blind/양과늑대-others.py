info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8],
          [6, 9], [9, 10]]

from collections import defaultdict

max_sheep = 0


def solution(info, edges):

    # 자식 저장
    child = defaultdict(list)
    for e in edges:
        child[e[0]].append(e[1])

    #print(child)

    def dfs(node, sheep, wolf, visited):
        global max_sheep

        #print("---dfs")
        #print(node)
        #print("visited ", visited)

        # 양 늑대 확인
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        if sheep <= wolf:
            #print("맛잇다 ", sheep, wolf)
            return
        
        # 양 최대값
        max_sheep = max(max_sheep, sheep)

        #print("sheepwolf max ", sheep, wolf, max_sheep)

        visited.append(node)

        # 방문노드의 모든 자식에 대해 재귀
        for v in visited:
            for c in child[v]:
                # 무한루프 방지
                if c not in visited:
                    #print("before", c,sheep,wolf)
                    dfs(c, sheep, wolf, visited[:])
                    #print("after", c, sheep, wolf)

    dfs(0, 0, 0, [])


    return (max_sheep)


print(solution(info1, edges1))