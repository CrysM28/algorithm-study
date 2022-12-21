def solution(answers):
    spj1 = [1,2,3,4,5]
    spj2 = [2,1,2,3,2,4,2,5]
    spj3 = [3,3,1,1,2,2,4,4,5,5]

    correct = [0] * 4

    for i, answer in enumerate(answers):
        if spj1[i%len(spj1)] == answer:
            correct[1] += 1
        if spj2[i%len(spj2)] == answer:
            correct[2] += 1
        if spj3[i%len(spj3)] == answer:
            correct[3] += 1

    answer = []
    max_correct = max(correct)

    for i in range(1,4):
        if correct[i] == max_correct:
            answer.append(i)

    return answer
