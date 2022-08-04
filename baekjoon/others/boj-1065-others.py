a = int(input())
if a < 100: print(a)    # 두자리수면 애초에 for문 돌릴 필요 X, 전부 한수
else:
    u = 99
    for i in range(100, a + 1):     # 자릿수 직접 비교
        if i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10: u += 1
    print(u)
