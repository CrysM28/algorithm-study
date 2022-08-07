n = int(input())
sg_cards = list(input().split())
m = int(input())
input_cards = list(input().split())
answer = [0] * m

for c in input_cards:
    if c in sg_cards:
        answer[input_cards.index(c)] = 1

print(answer)