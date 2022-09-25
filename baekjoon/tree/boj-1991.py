# 1991. 트리 순회

# NLR
def preorder(node):
    if node != '.':
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])

# LNR
def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])

# LRN
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")

n = int(input())

tree = dict()
for _ in range(n):
    n, l, r = input().split() 
    tree[n] = [l, r]

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()