# 15686. 치킨 배달
## 조합으로 푸는 문제...

# 도시 크기, 치킨집 최대 개수
n, m = map(int, input().split())

# 전체, 치킨집 위치, 집 위치
graph = []
chickens = []
houses = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 1:
            houses.append((i,j))
        elif t == 2:
            chickens.append((i,j))
    graph.append(tmp)

# print(*graph, sep="\n")
# print(chickens)
# print(houses)

# 각 치킨집에서의 집 거리 구하기
chicken_dist = dict()
for idx, c in enumerate(chickens):
    ci,cj = c
    chicken_dist[idx] = []

    for h in houses:
        hi, hj = h
        cdist = abs(ci-hi) + abs(cj-hj)
        chicken_dist[idx].append(cdist)

print(chicken_dist)


# 치킨가게 별 치킨거리 구하기
cdist_sum = []
for i, c in chicken_dist.items():
    cdist_sum.append([i, sum(c)])

# 치킨거리 정렬
cdist_sum.sort(key=lambda x:x[1])

print(cdist_sum)


# 다행히 안망하고 선택받은 m개의 치킨집
selected = []
for i in range(m):
    selected.append(cdist_sum[i][0])


# 남은 m개의 치킨집에서 치킨거리 최소값 구하기
min_cdist = 0

# 집별 최소거리
h_num = len(houses)
for h in range(h_num):  
    min_hdist = int(1e9)   
    for s in selected:
        min_hdist = min(min_hdist, chicken_dist[s][h])

    min_cdist += min_hdist

print(min_cdist)


'''
- 치킨 거리: 집(1)과 치킨집(2)까지의 거리

모든 집에서 최소가 되는 치킨집 거리를 구한 합
즉, 치킨집 폐업이 안 되는 조건에서는 집 기준으로 bfs 탐색을 해서 
치킨집을 찾아내서 그 거리를 더하면 됨

근데 지금은 치킨집이 폐업이 될 건데
즉 전체 c개 중에서 m개를 골랐을 때 치킨거리가 최소가 되는 값을 구해야 함

즉 어떤 지점을 없애도 되는지를 알아야함
그러면 각 집에서 모든 치킨집까지의 거리를 구해두고
dict 형태? 

{치킨집: [각 집 치킨거리]}

이렇게 해놓고 치킨거리배열 = (치킨집 #, 치킨거리합)으로 해놓은다음에
치킨거리합 최소로 정렬해서 
이 중 최소인 m개만 고르고
그 치킨집[m][i] 일 때 m마다 i가 최소인 값을 더해서 구하면 될 듯




- m개의 치킨집만 남기 때문에

각 치킨집에서 모든 집 까지의 거리를 계산하고
그 합이 가장 작은 


'''