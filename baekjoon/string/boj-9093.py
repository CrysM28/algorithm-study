# 9093. 단어 뒤집기

for _ in range(int(input())):
    sentence = list(input().split())    
    for s in sentence:
        print(s[::-1], end=" ")