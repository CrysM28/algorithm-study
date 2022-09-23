# 8:25 ~ 9:30 (<55분)
## 시간초과 처리때문에 8:50부터 더 처리
## 딴 문제 풀다가 와서 실제로는 약 40~45분

from collections import deque

# q1 = [3, 2, 7, 2]
# q2 = [4, 6, 5, 1]
q1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
q2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def solution(queue1, queue2):
    answer = -1

    # 효율을 위해 deque 사용
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 합이 홀수면 두 큐의 합이 같을 수가 없음 -> 바로 종료
    if (sum1 + sum2) % 2 != 0:
        return answer

    n = len(queue1) + len(queue2)
    cnt = 0
    while True:
        # 한 바퀴 다 돌았는데도 못 찾았으면 답 없음
        if cnt > 2 * n:
            return answer

        # 같으면 종료
        if sum1 == sum2:
            answer = cnt
            break
        
        # q2에서 빼서 q1로
        elif sum1 < sum2:
            val = queue2.popleft()
            sum2 -= val
            queue1.append(val)
            sum1 += val
            cnt += 1

        # q1에서 빼서 q2로
        else:
            val = queue1.popleft()
            sum1 -= val
            queue2.append(val)
            sum2 += val 
            cnt += 1

    return answer


print(solution(q1, q2))
