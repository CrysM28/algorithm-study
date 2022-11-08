def solution(s):    
    left = 0
    right = 0
    order = 0
    
    for ss in s:
        if ss == '(':
            left += 1
            order += 1
        else:
            right += 1
            order -= 1
        
        if order < 0:
            return False

    if right == left:
        return True
    else:
        return False