# 7579. 앱

N, M = map(int, input().split())
act = list(map(int, input().split()))
deact = list(map(int, input().split()))

app = []
for a, d in zip(act, deact):
    app.append([a, d])

print(app)