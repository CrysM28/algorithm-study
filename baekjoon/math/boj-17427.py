# 약수의 합 2
## 수학, 정수론

## 풀이 인터넷 참고
# 생으로 f, g 구하는건 무조건 타임아웃, 규칙을 찾아서 최적화해야 통과됨

n = int(input())
answer = 0

for i in range(1, n+1):
    answer += i * (n//i)

print(answer)