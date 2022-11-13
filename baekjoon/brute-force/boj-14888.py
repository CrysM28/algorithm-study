# 14888. 연산자 끼워넣기
INF = int(1e10)

N = int(input())
numbers = list(map(int, input().split()))
# [+, -, *, /] 개수
operators = list(map(int, input().split()))

max_ans = -INF
min_ans = INF

def dfs(i, result):
    global max_ans, min_ans

    if i == N:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return
    
    num = numbers[i]

    # +
    if operators[0] > 0:
        operators[0] -= 1
        dfs(i+1, result+num)
        operators[0] += 1

    # -
    if operators[1] > 0:
        operators[1] -= 1
        dfs(i+1, result-num)
        operators[1] += 1

    # *
    if operators[2] > 0:
        operators[2] -= 1
        dfs(i+1, result*num)
        operators[2] += 1
    # /
    if operators[3] > 0:
        operators[3] -= 1
        dfs(i+1, int(result/num))
        operators[3] += 1


dfs(1, numbers[0])

print(max_ans)
print(min_ans)
