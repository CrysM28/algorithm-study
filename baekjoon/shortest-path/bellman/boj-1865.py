# 1865. 웜홀

def time_slip():
    dist = [0] * (V + 1)

    # 벨만-포드
    for i in range(V):
        for a, b, c in edges:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                # 음수 사이클이 존재 
                if i == V - 1:
                    return True
    return False


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

    if time_slip():
        print("YES")
    else:
        print("NO")