def solution(n, lost, reserve):
    # 체육복 멀쩡히 있는 애들
    answer = n - len(lost)

    # 왼쪽부터 빌려줘야 가장 많이 빌려줄 수 있음, 혹시 모르니 오름차순 정렬
    lost.sort()
    reserve.sort()

    lost_tmp = lost[:]
    reserve_tmp = reserve[:]

    # 잃어버렸지만 여분 있는 애부터 걸러내기
    for l in lost:     
        if l in reserve:      
            reserve_tmp.remove(l) 
            lost_tmp.remove(l)
            answer += 1        

    lost = lost_tmp[:]
    reserve = reserve_tmp[:]

    for l in lost:          # 잃어버린 애가 빌릴 수 있는 애
        r1, r2 = l-1, l+1   # 앞뒤로 찾아보기
        if r1 in reserve:
            reserve.remove(r1)
            answer += 1
        elif r2 in reserve:
            reserve.remove(r2)
            answer += 1

    return answer

print(solution(5, [1,2,3,4,5], [1,2,3,4,5]))
#print(solution(5, [2,4], [1,3,5]))
#print(solution(10, [2,4,5,8], [3,5,6]))
#print(solution(6, [2,3,5], [1,2,4,6]))