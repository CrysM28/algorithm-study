from collections import defaultdict

# 전위순회
# NLR
def preorder(node, ans=[]):
    if node in tree:
        child = tree[node]
        if len(child) == 2:
            ans.append(node)
            preorder(tree[node][0], ans)
            preorder(tree[node][1], ans)
        elif len(child) == 1:
            ans.append(node)
            preorder(tree[node][0], ans)

    # leaf
    else:
        ans.append(node)

    return ans

# 중위순회
# LNR
def inorder(node, ans=[]):
    if node in tree:
        child = tree[node]
        if len(child) == 2:
            inorder(tree[node][0], ans)
            ans.append(node)
            inorder(tree[node][1], ans)
        elif len(child) == 1:
            inorder(tree[node][0], ans)
            ans.append(node)
    else:
        ans.append(node)
    return ans

# 후위순회
# LRN
def postorder(node, ans=[]):
    if node in tree:
        child = tree[node]
        if len(child) == 2:
            postorder(tree[node][0], ans)
            postorder(tree[node][1], ans)
            ans.append(node)
        elif len(child) == 1:
            postorder(tree[node][0], ans)
            ans.append(node)
    else:
        ans.append(node)
    return ans

######################################################

# 1~n인 완전이진트리 생성하기
n = int(input())
tree = defaultdict()
for i in range(1, n):
    left = i * 2
    right = left + 1

    if left > n:
        break
    elif right > n:
        tree[i] = [left]
        break
    tree[i] = [left, right]


pre1 = preorder(1)
in1 = inorder(1)
post1 = postorder(1)

print(pre1)
print(in1)
print(post1)