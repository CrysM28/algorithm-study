# 8:10 ~ 8:25 (15분)
from collections import defaultdict

s = ["AN", "CF", "MJ", "RT", "NA"]
c = [5, 3, 2, 7, 5]


def solution(survey, choices):
    answer = ''
    # 유형별 점수 저장
    ps = defaultdict(int)

    # 항목별 점수 계산
    for i in range(len(survey)):
        c = choices[i]

        # 선택지별 점수 가중치
        if c == 4:
            continue
        elif c < 4:
            s = survey[i][0]
        elif c > 4:
            s = survey[i][1]

        score = abs(c - 4)
        ps[s] += score

    # 성격유형 결과: R,T / C,F / J,M / A,N

    if ps['R'] >= ps['T']:
        answer += 'R'
    else:
        answer += 'T'

    if ps['C'] >= ps['F']:
        answer += 'C'
    else:
        answer += 'F'

    if ps['J'] >= ps['M']:
        answer += 'J'
    else:
        answer += 'M'

    if ps['A'] >= ps['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


print(solution(s, c))