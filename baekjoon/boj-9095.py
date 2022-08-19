# 9095. 1,2,3 더하기
## 0 < n < 11 이므로 brute-force로 풀어도 될 듯

for _ in range(int(input())):
    n = int(input())

    # 1로만 이루어진 경우로 시작
    added = [1 for _ in range(n)]
    cnt = 1

    # 1에서 2 묶기
    for i in range(n):
        add = added[:]
        try:
            add.pop(i)
            add.pop(i+1)
            cnt += 1
        except:
            continue

    print(cnt)