# 11657. 타임머신


def bellman_ford(start):
    dist = [INF] * (v + 1)  # 최단 거리 테이블
    dist[start] = 0  # 시작 노드 초기화

    # (정점-1)번 라운드
    for i in range(v):
        # 매 라운드마다 모든 간선을 확인
        for a, b, c in edges:
            # 현재 간선을 거쳐서 가는 거리가 더 짧은 경우
            if dist[a] != INF and dist[b] > dist[a] + c:
                # m번째에서 값이 갱신되면 음수 순환이 존재
                if i == v - 1: return -1
                dist[b] = dist[a] + c
    return dist


INF = int(10e9)

v, e = map(int, input().split())  # 도시(노드), 버스(간선) 수
edges = []  # 모든 간선에 대한 정보

# 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 벨만-포드
bf = bellman_ford(1)

# 출력
if bf == -1:
    print(bf)
else:
    for b in bf[2:]:
        if b >= INF:
            print(-1)
        else:
            print(b)