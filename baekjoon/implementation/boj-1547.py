# 1547. 공

cup = [1,2,3]

for i in range(int(input())):
    a, b = map(int, input().split())

    idx1 = cup.index(a)
    idx2 = cup.index(b)

    cup[idx1], cup[idx2] = b, a


print(cup[0])