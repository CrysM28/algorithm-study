import heapq as h

def solution(jobs):
    jobs.sort()

    answer = 0
    time = 0
    finished = 0
    i = 0
    work_q = []

    while finished < len(jobs):
        for job in jobs[i:]:
            start, duration = job
            i += 1
            if start < time:
                h.heappush(work_q, (duration, start))
            else:
                finished += 1
                time = duration + start
                answer += duration
                break
        
        #print(work_q, finished, time, answer)
        
        if work_q:
            d, s = h.heappop(work_q)
            answer += d + time - s
            time += d
            finished += 1
        
    print(work_q)
    print(work_q, finished, time, answer)
    print(answer // len(jobs))

def solution2(jobs):
    jobs.sort()

    answer = 0
    time = 0
    work_q = []
    
    for job in jobs:
        start, duration = job

        # 작업 중에 요청 들어오면 큐에 넣기
        if start < time:
            h.heappush(work_q, (duration, start))
        # 작업 중 아니고 큐에 작업 없으면 바로 처리
        else:
            if not work_q:
                time += duration
                answer += duration
                
        # 큐에 작업 있으면 새 작업이 겹칠 때까지 반복
        while work_q:
            d, s = h.heappop(work_q)

            if start < time + d:
                h.heappush(work_q, (duration, start))
                break

            time += d
            answer += time + s - d
                
    while work_q:
        d, s = h.heappop(work_q)
        time += d
        answer += time + s - d   

    
    print(work_q)

    print(time)
    print(answer)


# import heapq as h

# def solution(jobs):
#     jobs.sort()

#     time = 0
#     finished = 0
    
#     work_q = []
    
    
#     for job in jobs:
#         start, duration = job
#         if start < time:
#             h.heappush(work_q, duration)
#         else:
#             finished += 1
#             time += duration
    
#         if work_q:
#             t = h.heappop(work_q)
#             time += t
    
#     print(time)
    
#     while finished < len(jobs):
#         for job in jobs[finished:]:
#             start, takes = job

#             if start < time:
#                 h.heappush(work_q, takes)
#             else:
#                 finished += 1
#                 time += takes
        
#         print(time, finished, work_q)
#         break
        
        
        
#         for job in jobs[finished:]:
#             start, takes = job

#             if start < time:
#                 h.heappush(work_q, takes)
#             else:
#                 break
        
        
        
#         print(time)
#         print(work_q)    
        

