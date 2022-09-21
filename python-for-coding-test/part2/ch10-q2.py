# 팀 결성

# 같은 팀 확인
def find(x):
    if team[x] != x:
        team[x] = find(team[x])
    return team[x]

# 팀 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 쪽을 부모로 합치기
    if a < b:
        team[b] = a
    else:
        team[a] = b


# 학생 수, 연산 수
n, m = map(int, input().split())
team = [i for i in range(n+1)]

for _ in range(m):
    ops, a, b = map(int, input().split())

    if ops == 0:
        union(a, b)
    elif ops == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")