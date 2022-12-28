# 2212. 센서

N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

dist = []
for i in range(N-1):
    dist.append(sensors[i+1] - sensors[i])
dist.sort()

dist = dist[:(N-K)]

print(sum(dist))