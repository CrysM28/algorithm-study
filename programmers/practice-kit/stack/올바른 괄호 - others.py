def solution(s):    
    cnt = 0
    
    for ss in s:
        if ss == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            return False

    return cnt == 0