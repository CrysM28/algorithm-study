# 3:45~ 5:15 (1시간 30분..)

info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

info2=[0,1,0,1,1,0,1,0,0,1,0]
edges2=[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	



from collections import defaultdict


def solution(info, edges):

    # NLR
    def preorder(node, arr=[]):
        # N
        #print(node, end="-")
        arr.append(node)
        # L
        if len(tree[node]) > 0:
            preorder(tree[node][0], arr)
        # R
        if len(tree[node]) == 2:
            preorder(tree[node][1], arr)


    # LNR
    def inorder(node, arr=[]):
        # L
        if len(tree[node]) > 0:
            inorder(tree[node][0], arr)
        # N
        #print(node, end="-")
        arr.append(node)
        # R
        if len(tree[node]) == 2:
            inorder(tree[node][1], arr)


    # LRN
    def postorder(node, arr=[]):
        # L
        if len(tree[node]) > 0:
            postorder(tree[node][0], arr)
        # R
        if len(tree[node]) == 2:
            postorder(tree[node][1], arr)
        # N
        #print(node, end="-")
        arr.append(node)



    # 상수 처리
    SHEEP = 0
    WOLF = 1

    # 양, 늑대 연결 정보
    which = dict()  # 노드에 있는 게 무엇인지
    tree = defaultdict(list)  # 트리 형태

    for idx, i in enumerate(info):
        which[idx] = i
    for e in edges:
        a, b = e
        tree[a].append(b)

    print(which)
    print(tree)

    # 전중후 트리 순회
    pre_search, in_search, post_search = [],[],[]

    preorder(0, pre_search)
    inorder(0, in_search)
    postorder(0, post_search)

    print(pre_search)
    print(in_search)
    print(post_search)


    # 가능한 양의 수 찾기
    def search_sheep(arr):
        print("new")
        sheeps = 0
        wolves = 0

        for s in arr:
            
            if which[s] == SHEEP:
                sheeps += 1
            elif which[s] == WOLF:
                wolves += 1
            
            print(s, sheeps, wolves)

            if sheeps <= wolves:
                return sheeps


    sheep1 = search_sheep(pre_search)
    sheep2 = search_sheep(in_search)
    sheep3 = search_sheep(post_search)


    max_sheep = 0


    print(sheep1, sheep2, sheep3)






    answer = 0

    return answer


print(solution(info1, edges1))



    def bfs(start):
        dist = defaultdict(int)
        q = [(start, 1)]

        while q:
            print(q)
            node, animal = h.heappop(q)
            

            if node not in dist:
                dist[node] = animal
                for v, w in graph[node]:
                    alt = animal + w
                    q.append((v, alt))




            print("dist:", dist)


        return dist




    def backtrack(node, s, w):
        # count
        if which[node] == SHEEP:
            s += 1
        elif which[node] == WOLF:
            w += 1  
        print("--node--", node)
        print("sheep wolf", s, w)

        # 종료조건
        if s != 0 and s <= w:
            print("끝")
            visited.pop()
            return s, w

        for v in graph[node]:
            if v not in visited:

                visited.append(v)

                print("v", v, visited)

                s, w = backtrack(v,s,w)
                print("끝난뒤 animals", s, w)
                
                print("돌아가기", v, visited)
        
        return s, w
        # for i in range(len(info)):
        #     if i not in visited:
        #         visited.append(i)
        #         if which[i] == SHEEP:
        #             s += 1
        #         else:
        #             w += 1
        #         backtrack(s, w)
        #         visited.pop()
