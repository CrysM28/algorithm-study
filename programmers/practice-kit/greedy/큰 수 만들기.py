
def solution(number, k):
    number = list(map(int, number))
    
    ans = [number[0]]
    
    for i in range(1, len(number)):
        while ans and k != 0 and ans[-1] < number[i]:
            ans.pop()
            k -= 1
        ans.append(number[i])
        
        if k == 0:
            break
    
    ans += number[i+1:]

    while k != 0:
        ans.pop()
        k -= 1
    
    max_number = "".join(map(str,ans))
    return max_number



#print(solution("21613", 4))
print(solution("4177252841", 4))
#print(solution("8888844", 2))
#print(solution("88982199333", 4))
#print(solution("87654321", 3))

