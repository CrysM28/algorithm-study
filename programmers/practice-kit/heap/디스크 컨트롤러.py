import heapq as h

def solution(jobs):
    n = len(jobs)
    jobs.sort()

    start = -1
    end = 0
    
    queue = []
    done = 0
    total = 0
        
    while done < len(jobs):   
        for job in jobs:
            request, duration = job
            if start < request <= end:
                h.heappush(queue, (duration, request))
                        
        if queue:
            dur, req = h.heappop(queue)
            start = end
            end += dur
            total += end - req
            done += 1
        else:
            end += 1

        
    return (total //n)
    
    
    
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
#print(solution([[0, 3], [1, 9], [2, 6]]))