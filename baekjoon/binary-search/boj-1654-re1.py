# 1654. 랜선 자르기
## 매개변수 탐색 (parametric search)

def get_lan_num(cut_length):
    if cut_length == 0:
        cut_length = 1
        
    cut_num = 0
    for l in lans:
        cut_num += l // cut_length
    return cut_num


k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start, end = 0, max(lans)
ans = 0

while start <= end:
    length = (start + end) // 2
    num = get_lan_num(length)

    #print(start, end, length, num)

    # 더 길게 자를 수 있겠다
    if num >= n:
        ans = length
        start = length + 1
    
    # 더 짧게 잘라야겠다
    elif num < n:
        end = length - 1


print(ans)