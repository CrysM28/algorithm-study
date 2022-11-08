def solution(clothes):
    dic = dict()
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
        
    answer = 1
    for val in dic.values():
        answer *= (val + 1)
    
    return (answer - 1)