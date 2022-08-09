# input 처리
n, m = map(int, input().split())
dogam_list = [input() for _ in range(n)]
questions = [input() for _ in range(m)]

# 빠른 탐색이 가능한 dict 형태로 저장
dogam = dict()
for key, value in enumerate(dogam_list):
    dogam[key + 1] = value
reverse_dogam = {v: k for k, v in dogam.items()}

# 문제 답 말하기
for q in questions:
    if q.isdigit():
        print(dogam[int(q)])
    elif q.isalpha():
        print(reverse_dogam[q])
