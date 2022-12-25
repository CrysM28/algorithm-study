def solution(brown, yellow):
    answer = []
    
    for h in range(1, yellow+1):
        if yellow%h == 0:
            w = yellow // h
            if w < h:
                break
            if (w+2) * (h+2) == brown+yellow:
                answer = [w+2, h+2]
                break
    
    return answer