# 2798. 블랙잭
## 이전 풀이와 시간은 같으나 메모리가 더 효율적

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse = True)

blackjack = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum <= m and card_sum > blackjack:
                blackjack = card_sum

print(blackjack)