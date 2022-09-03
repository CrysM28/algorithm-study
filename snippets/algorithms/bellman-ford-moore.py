def bellman_ford(start):
    dist = [INF] * (V + 1)  # 최단 거리 테이블
    dist[start] = 0  # 시작 노드 초기화

    # (정점-1)번 라운드
    for i in range(V):
        # 매 라운드마다 모든 간선을 확인
        for a, b, c in edges:
            # 현재 간선을 거쳐서 가는 거리가 더 짧은 경우
            if dist[a] != INF and dist[b] > dist[a] + c:
                # V번째에서 값이 갱신되면 음수 순환이 존재한다는 뜻
                if i == V - 1: 
                    return -1
                dist[b] = dist[a] + c
    return dist


INF = int(10e9)

# 입력: 정점, 간선, 시작 노드
V, E, start = map(int, input().split()) 
edges = []  # 모든 간선에 대한 정보

# 간선 정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 벨만-포드
bf = bellman_ford(start)
print(bf)