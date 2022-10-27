# 25631. 마트료시카 합치기

n = int(input())
matryo = list(map(int, input().split()))

matryo.sort()
have = [False] * n
end = 0

for i in range(n):
    cur = matryo[i]

    for j in range(i+1, n):
        next = matryo[j]
        if cur < next and not have[j]:
            have[i] = False
            have[j] = True
            break
    else:
        end = n - i
        break

print(end)


