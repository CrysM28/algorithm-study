# 4949. 균형잡힌 세상

while True:
    stack = []
    answer = 'yes'

    sentence = input()
    if sentence == '.':
        break

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
    
    if stack:
        answer = 'no'
    

    print(answer)




