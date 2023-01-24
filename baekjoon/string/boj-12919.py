# 12919. A와 B 2
from collections import deque

S = input()
T = input()

queue = deque([T])
same = False

while queue:
    word = queue.popleft()

    if word == S:
        same = True
        break

    if len(word) < len(S):
        break

    if word[-1] == 'A':
        queue.append(word[:-1])
    if word[0] == 'B':
        queue.append(word[1:][::-1])

if same:
    print(1)
else:
    print(0)

