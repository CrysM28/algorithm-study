# 13458. 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for students in A:
    students -= B
    answer += 1
    if students > 0:
        answer += (students-1) // C + 1
    
print(answer)