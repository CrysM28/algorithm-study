# 1043. 거짓말
from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# input
people_num, party_num = map(int, input().split())
who_knows = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(party_num)]

# union-find
## 초기화: 부모가 자기 자신
parent = defaultdict(int)
for i in range(1, people_num + 1):
    parent[i] = i

## x의 root 노드 찾기
def find(x):
    if parent[x] != x:  # x가 root가 아닌 자식 노드인 경우,
        parent[x] = find(parent[x])  # 부모 노드에 대해 재귀 실행
        # + path compression: find 하며 만난 모든 값의 부모 노드를 root로
    # x가 root면 그대로 반환
    return parent[x]

## a, b 합치기
def union(a, b):
    # 각각의 root 노드 찾기
    a = find(a)
    b = find(b)

    # 집합 합치기
    parent[b] = a


# party!
lie = 0  # 거짓말 장전

# 아무도 모르면 모든 파티에서 거짓말 가능
if who_knows[0] == 0:
    lie = party_num

else:
    # 1. 거짓말 아는사람끼리 먼저 union
    know_root = who_knows[1]
    for w in who_knows[1:]:
        union(know_root, w)

    # 2. 파티마다 만난 사람 union
    for p in party:
        if p[0] > 1:
            for pp in p[2:]:
                union(p[1], pp)

    # 3. 파티마다 아는지 확인
    for p in party:
        know = False

        for pp in p[1:]:
            # 아는 사람 있으면 거짓말 X
            if find(pp) == find(know_root): 
                know = True
                break

        # 아는 사람 없었으면 거짓말 O    
        if not know:
            lie += 1

print(lie)
