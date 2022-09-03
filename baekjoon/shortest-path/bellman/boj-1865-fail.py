# 1865. 웜홀
## 시간 초과


def time_slip(start):
    # 최단거리 테이블
    dist = [INF] * (V + 1)
    dist[start] = 0

    # 출발지점으로 돌아올 수 있는지
    cycle = False

    # 매 라운드마다 모든 간선 확인
    for i in range(V):
        for a, b, c in edges:
            # 현재 간선을 거쳐서 가는 거리가 더 짧은 경우
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == V - 1:
                    cycle = True

    # 출발지점으로 돌아올 수 있고 시간이 되돌아갔으면
    # 사실 cycle 생긴 것 자체가 음수 사이클이므로 굳이 -인지 확인하지는 않아도 됨
    if cycle and dist[start] < 0:   
        return True

    return False


def result():
    for i in range(1, V + 1):  # 각 정점마다 확인 ## 이 부분에서 시간초과 남
        ts = time_slip(i)
        if ts:
            return "YES"
    return "NO"



INF = int(10e9)

for _ in range(int(input())):
    # 지점, 도로, 웜홀 개수
    V, E, W = map(int, input().split())

    # 연결 정보
    edges = []

    # 도로 - 양방향
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))


    # 웜홀 - 단방향
    for _ in range(W):
        a, b, c = map(int, input().split())
        edges.append((a, b, (-1) * c))

    print(result())