## 인터넷 참고

def solution(numbers, target):
    answer = 0
    
    # BFS 형태
    leaf = [0]  # 리프 노드만 저장
    for n in numbers:
        tmp = []
        for parent in leaf:
            tmp.append(parent + n)
            tmp.append(parent - n)
        leaf = tmp 

    # 최종 결과 확인
    for l in leaf:
        if l == target:
            answer += 1

    return answer

print(solution([4,1,2,1], 4))