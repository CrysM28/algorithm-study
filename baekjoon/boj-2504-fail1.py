
parenthesis = input()

open = ['(', '[']
close = [')', ']']
stack = []

temp_score = 1  # 곱셈
temp_sum = 0    # 덧셈
total_sum = 0


for p in parenthesis:
    # print(temp_score)
    # print(temp_sum)
    # print(total_sum)
    
    # print("=", p)

    # stack이 비어있고 close면 틀린 괄호열
    if not stack and p in close:
        total_sum = 0
        break

    if p in open:
        stack.append(p)

        # 이미 계산중인 괄호열이 있다면 덧셈 영역으로 옮기기        
        if temp_score > 1:
            temp_sum += temp_score
            temp_score = 1
    
    elif p in close:
        if not stack:
            continue

        s = stack.pop()
        
        # 점수 계산
        cur_score = 0
        if s == '(' and p == ')':
            cur_score = 2
        elif s == '[' and p == ']':
            cur_score = 3

        # 다른 모양이면 올바른 괄호열이 아님
        if cur_score == 0:
            total_sum = 0
            break
            # if temp_score == 1:
            #     temp_score = 0
            # total_sum +=  temp_score + temp_sum

            # # 초기화
            # temp_score = 1
            # temp_sum = 0
            # stack.clear()

        # 중간 점수 계산
        if stack:
            temp_score *= cur_score
        # 매치 후 stack이 비면 한 묶음 끝
        else:  
            total_sum += cur_score * (temp_score + temp_sum)
            temp_score = 1
            temp_sum = 0

    

print(total_sum)







############


parenthesis = input()

open = ['(', '[']
close = [')', ']']

stack = []
ops = []
scores = []
history = []

wrong = False

for p in parenthesis:
    # 틀린 괄호열
    if not stack and p in close:
        total_sum = 0
        wrong = True
        break

    if p in open:
        stack.append(p)

        if history:
            # 이전이 연속이면 곱하기
            if history[-1] in open:
                ops.append('*')
            # 이전에 하나 끝났으면 더하기
            elif history[-1] in close:
                ops.append('+')
    
    elif p in close:
        top = stack.pop()
        
        # 점수 계산
        cur_score = 0
        if top == '(' and p == ')':
            cur_score = 2
        elif top == '[' and p == ']':
            cur_score = 3

        # 틀린 괄호열
        if cur_score == 0:
            wrong = True
            total_sum = 0
            break

        scores.append(cur_score)
        #ops.append('+')

    print("==")
    print(history)
    print(ops)
    print(scores)

    history.append(p)


if wrong:
    print(0)
else:
    ans = scores[0]
    for i in range(1, len(scores)):
        cur_ops = ops.pop()

        if cur_ops == '+':
            ans += scores[i]
        elif cur_ops == '*':
            ans *= scores[i]
        
        print(ans)
    
    print(ans)
        



