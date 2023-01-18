# 같은 로직인데 살짝 다르게 푼 풀이

n = int(input())
nums = list(map(int, input().split()))
s = 0
e = n - 1
com = [nums[0], nums[e]]
minimum = 10**10

while s < e:
    if abs(nums[s] + nums[e]) <= minimum:
        com = [nums[s], nums[e]]
        minimum = abs(sum(com))
    
    # 어차피 오름차순이니까 이런 경우는 s가 음수고 e가 양수인 경우 뿐이므로
    if abs(nums[s]) > abs(nums[e]):
        s += 1
    else:
        e -= 1
    
    # 하지만 0이 됐을때 바로 빠져나오는 구간이 없어 시간 손해 조금 있을지도
    ## 채점 상으로는 12ms 정도 차이만 나긴 함


print(*com)