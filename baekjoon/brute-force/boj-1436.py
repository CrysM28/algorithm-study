# 1436. 영화감독 숌

# 숫자 순서대로 생성하는 generator
def numbers_generator():
    count = 665
    while True:
        count += 1
        yield str(count)


n = int(input())
cnt = 0
numbers = numbers_generator()

while True:
    num = next(numbers)
    if "666" in num:
        cnt += 1
    if cnt == n:
        break

print(num)


