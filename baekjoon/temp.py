# for easy problems

chess = [1,1,2,2,2,8]
white = list(map(int, input().split()))

for i in range(len(white)):
    chess[i] -= white[i]

print(chess)
