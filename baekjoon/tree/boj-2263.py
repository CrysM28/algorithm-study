# 2236. 트리의 순회
import sys

sys.setrecursionlimit(10**5)

n = int(input())
inorder_tree = list(map(int, input().split()))
postorder_tree = list(map(int, input().split()))
preorder_tree = []


# 분할정복
def recursive(in_start, in_end, post_start, post_end):

    # 종료 조건
    if in_start > in_end or post_start > post_end:
        return

    # 후위: 마지막 = root
    root = postorder_tree[post_end]
    preorder_tree.append(root)

    # 중위: root 기준으로 L/R 서브트리
    left_idx = -1
    right_idx = -1
    for i in range(in_start, in_end+1):
        if inorder_tree[i] == root:
            left_idx = i - in_start
            right_idx = in_end - i
            break
    if left_idx == -1 or right_idx == -1:
        return

    # 나눈 L/R 서브트리에 대해 똑같이 수행
    recursive(in_start, in_start+left_idx-1, post_start, post_start+left_idx-1)
    recursive(in_end-right_idx+1, in_end, post_end-right_idx, post_end-1)


recursive(0, n-1, 0, n-1)

print(*preorder_tree)