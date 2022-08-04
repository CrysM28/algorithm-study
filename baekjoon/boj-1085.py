x, y, w, h = map(int, input().split())
distance = min(abs(x-w), abs(y-h), x, y)
print(distance)