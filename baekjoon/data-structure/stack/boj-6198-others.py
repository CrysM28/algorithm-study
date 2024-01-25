
N = int(input())
building = [int(input()) for _ in range(N)]

ans = 0
stack = []

for i in range(N):

    while stack and building[i] > stack[-1]:
        stack.pop()
    stack.append(building[i])

    # 스택에 있는 건물은 모두 현재 빌딩을 볼 수 있음
    ans += len(stack) -1

print(ans)


