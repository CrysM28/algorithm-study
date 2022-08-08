# 4:15 ~ 3:45 -> 30분


def solution(dartResult):
    answer = 0
    prev_num = 0
    prev_score = 0
    score = 0

    for d in dartResult:
        if d.isnumeric():
            prev_score = score
            number = int(d)
            if prev_num == 1 and number == 0:
                number = 10
            prev_num = number

        elif d == 'S':
            score = number
            answer += number
            prev_num = 0

        elif d == 'D':
            score = number**2
            answer += score
            prev_num = 0

        elif d == 'T':
            score = number**3
            answer += score
            prev_num = 0

        elif d == '*':
            answer += (prev_score + score)
            score *= 2
            prev_score *= 2

        elif d == '#':
            answer += score * (-2)
            score *= -1

    return answer


#print(solution("1S2D*3T"))
#print(solution("1D2S#10S"))
#print(solution("1D2S3T*"))
print(solution("1D#2S*3S"))

