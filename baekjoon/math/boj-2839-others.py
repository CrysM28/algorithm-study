n = int(input())
count_3 = 0

# 5로 처리할 수 있을 때까지 3만큼
# 3, 5 동시에 나눌 수 있으면 5로 카운트됨
while n % 5 != 0:   
    n -= 3
    count_3 += 1
    if n < 0:
        print(-1)
        break

if n >= 0:
    print(f'{n//5 +  count_3}')
