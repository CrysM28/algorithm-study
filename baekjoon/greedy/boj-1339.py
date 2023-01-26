# 1339. 단어 수학
from collections import defaultdict

alph_to_num = defaultdict(int)
digit = 9
total = 0

N = int(input())

for _ in range(N):
    data = input()
    data = data[::-1]
    for i, d in enumerate(data):
        alph_to_num[d] += 10**i

words = sorted(alph_to_num.items(), key = lambda x:x[1], reverse = True)

for word in words:
    w = word[1]
    total += w * digit
    digit -= 1

print(alph_to_num)
print(total)
