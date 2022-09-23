# 8:25 ~
## 시간초과 

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
    total_sum = sum1 + sum2
    if total_sum % 2 != 0:
        return answer


    cnt = 0
    while True:
        # 답 찾기 전에 하나의 큐가 비어버리면 합 만들기 불가능
        if not queue1 or not queue2:
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
