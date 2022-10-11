# 10610. 30
# 30의 배수 = 3의 배수 & 10의 배수

n = list(map(int, input()))
n.sort(reverse=True)

answer = ''.join(map(str, n))

# 3의 배수 될 수 없으면
if sum(n) % 3 != 0:
    answer = -1

# 10의 배수 될 수 없으면
if n[-1] != 0:
    answer = -1
    
print(answer)