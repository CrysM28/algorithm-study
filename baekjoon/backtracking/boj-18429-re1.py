# 18429. 근손실

N, K = map(int, input().split())
A = list(map(int, input().split()))

routine = []
used = [False for _ in range(N)]
ans = 0


def backtrack(weight):
    global ans

    # 조건 탈락
    if weight < 500:
        return

    # 종료조건
    if len(routine) == N:
        ans += 1
        return
    
    # 운동해보기
    for i in range(N):
        if not used[i]:
            routine.append(i)
            used[i] = True
            weight += A[i]

            backtrack(weight - K)
            
            routine.pop()
            used[i] = False
            weight -= A[i]


backtrack(500)
print(ans)


'''
난이도: 실버 3
분류: 브루트포스, 백트래킹
시간: 15분

요약
- 운동 순서를 일일이 순열(combination)으로 만들어보며,
  중간에 조건 불만족(근 500이하) 시 종료하면서
  최종 조건 만족하면 카운트

풀이
- 사용 알고리즘
    - 어떤 조건을 만족하는 모든 경우의 수 -> 브루트포스
    - N 크기가 작으므로(<=8) -> 백트래킹
- 조건 불만족(weight < 500)일땐 바로 종료,
  종료 조건 만족 시(routine 완성, len==N)엔 카운트 증가,
  그 외에는 운동 진행하도록
- 체크 시에는 list의 in 연산보다 TF 배열을 두는 것이 시간 효율상 훨씬 좋음

'''