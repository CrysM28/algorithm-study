n = int(input())
sg_cards = set(input().split())
m = int(input())
input_cards = list(input().split())

for c in input_cards:
    if c in sg_cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
       

