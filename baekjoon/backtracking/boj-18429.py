# 18429. 근손실

N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
order = []

def backtrack():
    global answer

    if len(order) == N:
        weight = 500
        #print(order)
        for o in order:
            weight = weight - K + A[o]
            #print(weight)
            if weight < 500:
                break
        else:
            answer += 1
        
        return
    
    for i in range(N):
        if i not in order:
            order.append(i)
            backtrack()
            order.pop()


backtrack()

print(answer)