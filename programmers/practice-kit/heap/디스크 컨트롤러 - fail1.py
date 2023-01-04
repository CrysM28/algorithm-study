def solution(jobs):
    jobs.sort(key = lambda x: x[1])
    
    answer = 0
    end = 0
    for job in jobs:
        answer += job[1]
        if end > job[0]:
            answer += end - job[0]
        end += job[1]
        
    return answer // len(jobs)





'''
대충만 봤는데도 생긴게 딱 얼마전에 풀었던 greedy + heap 문제 같다

계속 업데이트를 해줘야 하는 건가?



'''