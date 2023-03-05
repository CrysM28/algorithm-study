# 17413. 단어 뒤집기 2

sentence = input()
stack = []
tag = False

for s in sentence:
    if tag:
        print(s, end="")
        if s == '>':
            tag = False
        continue
    
    if s == '<' or s == ' ':
        if stack:
            while stack: print(stack.pop(), end="")
        print(s, end="")
        if s == '<': tag = True
    else:
        stack.append(s)

if stack:
    while stack:
        print(stack.pop(), end="")
