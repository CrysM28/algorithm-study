# 17828. 문자열 화폐

N, X = map(int, input().split())
money = []

cur_X = X
for i in range(N):
    print(i)
    if cur_X <= 0:
        break

    if cur_X > 26 and cur_X-26 > N-i:
        money.append(26)
        cur_X -= 26
    else:
        for j in range(N-i-1, -1, -1):
            if cur_X - j > 26:
                money.append(26)
                cur_X -= 26
            else:
                if cur_X - j > 0:
                    money.append(cur_X - j)
                    money += [1] * j
                break
        break
    
print(money)

ascii_A = ord('A') - 1

if len(money) != N or sum(money) != X:
    print("!")
else:
    for i in range(N-1, -1, -1):
        cur_money = money[i]
        print(chr(cur_money+ascii_A), end='')


