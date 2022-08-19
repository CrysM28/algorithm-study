# 1918. 후위 표기식
## 나중에 다시 풀면서 더 깔끔하게 고쳐보자
equation = list(input())

prior = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 연산자 우선순위
stack = []  # 연산자 보관 스택
postfix = ""  # 후위연산자 변환결과

for e in equation:
    #print("== before ops:", e)
    #print(postfix, stack)

    ## 알파벳이면 문자열 추가
    if e.isalpha():
        postfix += e
        continue

    ## 연산자 처리
    # 스택이 비었으면 그냥 push
    if not stack and e != ')':
        stack.append(e)
        continue

    s = stack.pop()

    #print("==s, e:", s, e)

    # 왼괄호 ( 면 그냥 push
    if e == '(':
        stack.append(s)
        stack.append(e)

    # 오른괄호 ) 면 왼괄호 ( 나올 때까지 pop
    elif e == ')':
        while s != '(':
            postfix += s
            if stack: s = stack.pop()
            else: break

    # 스택의 연산자보다 우선순위가 높으면 push
    elif prior[e] > prior[s]:
        stack.append(s)
        stack.append(e)

    # 스택의 연산자보다 우선순위가 낮거나 같으면 계속 pop
    elif prior[e] <= prior[s]:
        while prior[e] <= prior[s]:
            if s != '(':
                postfix += s
            if stack: s = stack.pop()
            else: break
        if prior[e] > prior[s]:  # while 끝나고 조건 만족 안한 s는 다시 push
            stack.append(s)

        stack.append(e)  # pop 다 끝나면 현재 연산자 push

# 끝났으면 스택에 남은 것 모두 pop
while stack:
    s = stack.pop()
    if s != '(':
        postfix += s

print(postfix)
