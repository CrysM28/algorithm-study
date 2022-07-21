# 약수는 항상 가장 작은 것과 큰 것의 곱인것을 이용

input1 = input()
divisor = list(map(int, input().split()))
divisor.sort()

num2 = divisor.pop()

# 약수가 하나뿐인 경우
try:
    num1 = divisor.pop(0)
except:
    num1 = num2

print(num1*num2)