# 괄호

n = int(input())

for _ in range(n):
    ps = input()
    stack = list()      # 짝 체크용 스택: 매번 초기화

    for p in ps:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if(len(stack) == 0):
                break
            stack.pop()
    else:   # break 없이 끝까지 수행했을 때 스택이 비었으면 VPS
        if(len(stack) == 0):
            print('YES')
            continue
    
    print('NO')     # break 했거나 stack이 비어있지 않으면 VPS 아님