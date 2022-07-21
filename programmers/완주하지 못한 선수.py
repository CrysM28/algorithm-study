def solution(participant, completion):
    participant.sort()
    completion.sort()

    # 정렬 후 비교했을 때, 같은 인덱스에 다른 값이 있으면 그 part가 중복이면서 comp에 없는 사람
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 위 조건에 해당되지 않으면 가장 마지막이 comp에 없는 사람
    return participant[len(participant)-1]