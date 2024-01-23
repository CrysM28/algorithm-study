# 성적이 낮은 순서로 학생 출력하기

n = int(input())
arr = [input().split() for _ in range(n)]

arr.sort(key=lambda x: x[1])

for a in arr:
    print(a[0], end=" ")
