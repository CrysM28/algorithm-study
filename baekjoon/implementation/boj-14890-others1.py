n, l = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def solve(li):
    for i in range(1, n):
        # 1차이 나는 지 확인
        if abs(li[i-1] - li[i]) > 1:
            return False

        if li[i-1] < li[i]:
            for j in range(l):
                if i-1-j < 0 or li[i-1] != li[i-1-j] or check[i-1-j]:
                    return False
                if li[i-1] == li[i-1-j]:
                    check[i-1-j] = True
        elif li[i-1] > li[i]:
            for j in range(l):
                if i+j >= n or li[i+j] != li[i] or check[i+j]:
                    return False
                if li[i] == li[i+j]:
                    check[i+j] = True

    return True


answer = 0
for i in range(n): # 가로 줄 확인
    check = [False] * n
    if solve([graph[i][j] for j in range(n)]):
        answer += 1


for j in range(n): # 세로 줄 확인
    check = [False] * n 
    if solve([graph[i][j] for i in range(n)]):
        answer += 1

print(answer)