# 3:43~

info1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3],
          [6, 5], [4, 6], [8, 9]]

from collections import defaultdict


def solution(info, edges):



    # NLR
    def preorder(node, s, w, end):

        # N: 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1

        print("now in ", node, "with s w", s, w)
        
        # 잡아먹히는지 확인
        if s <= w:
            print("wovles")
            end = True

        if end:
            return s, w

        if len(tree[node]) > 0:
            # L
            print("going L")
            s, w = preorder(tree[node][0], s, w, end)
            print("back from L")
            # R
            if len(tree[node]) == 2:
                print("going R")
                s, w = preorder(tree[node][1], s, w, end)
                print("back from R")



    # NLR
    def preorder(tree, node, sheeps, wolves):
        if node != '.':
            print(node, end="")
            preorder(tree[node][0])
            preorder(tree[node][1])

    # LNR
    def inorder(tree, node, sheeps, wolves):
        if node != '.':
            inorder(tree[node][0])
            print(node, end="")
            inorder(tree[node][1])

 
 
     # LNR
    def inorder(node, s, w, end):
        # 잡아먹혔으면 끝
        if end:
            return
        
        # 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1
        print("now in ", node, "with s w", s, w)


        if len(tree[node]) > 0:
            # L
            print("L")
            s, w = inorder(tree[node][0], s, w, end)
            print("N")

            # N
            if s <= w:
                end = True
            print("R")
            
            # R
            if len(tree[node]) == 2:
                s, w = inorder(tree[node][1], s, w, end)

        return s, w

    # LRN
    def postorder(node, s, w, end):
        # 잡아먹혔으면 끝
        if end:
            return
        
        # 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1

        print("now in ", node, "with s w", s, w)

        # L
        if len(tree[node]) == 1:
            s, w = postorder(tree[node][0], s, w, end)

        # LR
        elif len(tree[node]) == 2:
            s, w = postorder(tree[node][0], s, w, end)
            s, w = postorder(tree[node][1], s, w, end)


        # N
        print("N")

        if s <= w:
            print("more wolves", node, s, w)
            end = True

        return s, w

    # 상수 처리
    SHEEP = 0
    WOLF = 1

    # 양, 늑대의 수
    sheeps = 0
    wolves = 0

    # 양, 늑대 연결 정보
    which = dict()  # 노드에 있는 게 무엇인지
    tree = defaultdict(list)  # 트리 형태

    for idx, i in enumerate(info):
        which[idx] = i

    for e in edges:
        a, b = e
        tree[a].append(b)

    tree[-1].append(1)

    print(which)
    print(tree)

    a = postorder(0, 0, 0 ,False)

    print(a)

    answer = 0

    return answer


print(solution(info1, edges1))




    # NLR
    def preorder(node, s, w, end):
        # 잡아먹히는지 확인
        if s!= 0 and s <= w:
            end = True
        if end:
            return s, w

        # N: 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1

        if len(tree[node]) > 0:
            # L
            s, w = preorder(tree[node][0], s, w, end)
            # R
            if len(tree[node]) == 2:
                s, w = preorder(tree[node][1], s, w, end)

        return s, w


    # LNR
    def inorder(node, s, w, end):
        # 잡아먹히는지 확인
        if end:
            return s, w

        # N: 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1       

        print("now in ", node, "with s w", s, w)




        if len(tree[node]) > 0:
            # L
            s, w = inorder(tree[node][0], s, w, end)


            if s!= 0 and s <= w:
                end = True


            # R
            if len(tree[node]) == 2:
                s, w = inorder(tree[node][1], s, w, end)

        return s, w




    # LRN
    def postorder(node, s, w, end):
        if end:
            return


        if len(tree[node]) > 0:
            # L
            s, w = postorder(tree[node][0], s, w, end)
            # R
            if len(tree[node]) == 2:
                s, w = postorder(tree[node][1], s, w, end)


        print("now in ", node, "with s w", s, w)



        # N: 노드 정보
        now = which[node]
        if now == SHEEP:
            s += 1
        elif now == WOLF:
            w += 1



        # 잡아먹히는지 확인
        if s <= w:
            end = True


        return s, w

