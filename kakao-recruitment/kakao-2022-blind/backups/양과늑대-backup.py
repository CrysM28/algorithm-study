# 3:45~ 5:15 (1시간 30분..)

info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

info2=[0,1,0,1,1,0,1,0,0,1,0]
edges2=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	



from collections import defaultdict, deque
import heapq as h

def solution(info, edges):

    # 상수
    SHEEP = 0
    WOLF = 1
    INF = int(1e9)

    def bfs(start):
        visited = {start}
        queue = deque([[start, 1]])

        finished = 1    # 0이 되면 끝
        sheep = 0

        while queue:
            # 1: 양, -1: 늑대
            print(queue)
            node, animal = queue.popleft()

            if animal == 1:
                sheep += 1

            finished += animal
            if finished == 0:
                break

            for v, w in tree[node]:
                if v not in visited:
                    visited.add(v)
                    queue.append([v,w])

            

        print(finished, sheep, visited)
        return visited

    # DFS: 스택 구현
    def dfs(start):
        visited = set()
        stack = [[start, 1]]

        finished = 1    # 0이 되면 끝
        sheep = 0

        while stack:
            node, animal = stack.pop()

            if animal == 1:
                sheep += 1

            finished += animal
            if finished == 0:
                break

            if node not in visited:
                visited.add(node)
                for v, w in tree[node]:
                    stack.append([v,w])
        print(finished, sheep, visited)

        return visited




    # 양, 늑대 연결 정보
    which = dict()  # 노드에 있는 게 무엇인지
    for idx, i in enumerate(info):
        which[idx] = i

    tree = defaultdict(list)  # 트리 형태
    for e in edges:
        a, b = e
        if which[b] == SHEEP:   # 양
            tree[a].append((b, 1))
        else:   # 늑대
            tree[a].append((b, -1))

    print(tree)



    bfs(0)
    dfs(0)

    answer = 0

    return answer


print(solution(info1, edges1))