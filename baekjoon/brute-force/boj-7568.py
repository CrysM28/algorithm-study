n = int(input())

weight, height = [], []
rank = [0] * n

# input
for _ in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)

# compare
for i in range(n):
    bigger = 0

    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            bigger += 1

    rank[i] = bigger + 1

print(*rank)