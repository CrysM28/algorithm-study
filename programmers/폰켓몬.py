def solution(nums):
    # 중복 제거 후 개수를 N/2와 비교해서 더 큰 값    
    can_take = len(nums)/2
    no_rep = len(set(nums))    
    
    if can_take > no_rep:
        answer = no_rep
    else:
        answer = can_take
    
    return answer