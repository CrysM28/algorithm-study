# 2042. 구간 합 구하기

import sys
input = sys.stdin.readline
 
# 세그먼트 트리 생성
# node가 담당하는 구간 [start, end]
def init(node, start, end): 
    # node가 리프 노드면 배열의 원소 값을 가짐
    if start == end :
        tree[node] = numbers[start]
        return tree[node]
    else :
        # LR 자식 트리를 재귀적으로 만들고 합을 저장
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
 
# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def subSum(node, start, end, left, right) :
    
    # 겹치지 않는 구간
    if left > end or right < start :
        return 0
 
    # 구간 안에 포함될 경우
    if left <= start and end <= right :
        return tree[node]
 
    # LR 자식을 루트로 하는 트리에서 다시 탐색 시작
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)
 
 
def update(node, start, end, index, diff) :
    if index < start or index > end :
        return
 
    tree[node] += diff
    
    # 자식도 변경
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
 
 
n, m, k = map(int, input().rstrip().split())
numbers = [int(input().rstrip()) for _ in range(n)]
tree = [0] * 3000000

# 세그먼트 트리 생성
init(1, 0, n-1)
 
for _ in range(m+k) :
    a, b, c = map(int, input().rstrip().split())

    # 값 변경
    if a == 1 :
        b = b-1
        diff = c - numbers[b]
        numbers[b] = c
        update(1, 0, n-1, b, diff)
    
    # 구간 합 구하기
    elif a == 2 :                
        print(subSum(1, 0, n-1 ,b-1, c-1))
