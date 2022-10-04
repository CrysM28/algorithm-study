# 2236. 트리의 순회
## 메모리 초과 -> 리스트 슬라이싱 때문
import sys
sys.setrecursionlimit(10**5)

n = int(input())
inorder_tree = list(map(int, input().split()))
postorder_tree = list(map(int, input().split()))
preorder_tree = []

# 분할정복
def recursive(inorder, postorder):
    # 종료 조건: 더 볼 게 없을때
    if not inorder:
        return

    # 후위: 마지막 = root
    root = postorder[-1]
    preorder_tree.append(root)

    # 중위: root 기준으로 L/R 서브트리
    for i in range(len(inorder)):
        if inorder[i] == root:
            in_left = inorder[:i]
            in_right = inorder[i+1:]
            post_left = postorder[:i]
            post_right = postorder[i:-1]
            break
    
    # 나눈 L/R 서브트리에 대해 똑같이 수행
    recursive(in_left, post_left)
    recursive(in_right, post_right)


recursive(inorder_tree, postorder_tree)
print(*preorder_tree)