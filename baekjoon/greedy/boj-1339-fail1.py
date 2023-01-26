# 1339. 단어 수학
## 나타난 비율도 고려했어야

words = [list() for _ in range(8)]
alph_to_num = dict()

N = int(input())
for _ in range(N):
    data = input()
    data = data[::-1]
    for i, d in enumerate(data):
        words[i].append(d)

digit = 9
total = 0

for i in range(7, -1, -1):
    if not words[i]:
        continue
    
    for w in words[i]:
        if w in alph_to_num:
            total += alph_to_num[w] * (10**i)
        else:
            alph_to_num[w] = digit
            total += digit * (10**i)
            digit -= 1

print(words)
print(alph_to_num)
print(total)



'''
1. 자릿수 별로 각각 배열에 넣음
2. 가장 큰 자릿수부터 할당
 

'''