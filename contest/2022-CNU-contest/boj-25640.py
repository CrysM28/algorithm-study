# 25640. MBTI

jinho = input()
n = int(input())

same = 0
for _ in range(n):
    friends = input()
    if friends == jinho:
        same += 1

print(same)