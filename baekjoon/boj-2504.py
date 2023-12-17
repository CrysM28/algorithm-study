
parenthesis = input()

open = ['(', '[']
close = [')', ']']

stack = []
ops = []
scores = []
history = []

wrong = False

tmp = 1
total = 0

for p in parenthesis:
    # open
    if p == '(':
        stack.append(p)
        tmp *= 2

    elif p == '[':
        stack.append(p)
        tmp *= 3

    # close
    elif p == ')':
        if not stack or stack[-1] != '(':
            total = 0
            break

        stack.pop()

        if stack:
            total += tmp
        
        tmp //= 2

    elif p == ']':
        if not stack or stack[-1] != '[':
            total = 0
            break
        stack.pop()
        if stack:
            total += tmp
        tmp //= 3

    print(p)
    print(total)



if stack:
    print(0)
else:
    print(total)
