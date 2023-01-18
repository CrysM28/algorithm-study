def solution(people, limit):
    people.sort()
    n = len(people)
    
    answer = n
    start = 0
    end = n-1
    
    while start < end:
        if people[start] + people[end] > limit:
            end -= 1
        else:
            answer -= 1
            start += 1
            end -= 1
    
    return answer