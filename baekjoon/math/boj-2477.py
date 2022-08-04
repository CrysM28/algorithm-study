k = int(input())

x, y = [], []
square = []

for i in range(6):
    pos, length = map(int, input().split())
    square.append([pos, length])

#for _ in range(6):

# length는 들어온 순서대로 유지할 수 있게 pos로만 정렬
square.sort(key=lambda x: x[0])
print(square)



#area = (max(x) * max(y)) - (2)
#print(area * k)
