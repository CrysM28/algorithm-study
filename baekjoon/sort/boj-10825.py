# 10825. 국영수

# 이름, 국영수 점수
students = []
for _ in range(int(input())):
    students.append(input().split())

# 조건
## 국어 내림차순
## 영어 오름차순
## 수학 내림차순
## 이름 오름차순

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in students:
    print(s[0])
