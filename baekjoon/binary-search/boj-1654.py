# 1654. 랜선 자르기
## 매개변수 탐색 (parametric search) 문제


def get_lan_num(cut_length):
    cut_num = 0
    for l in lans:
        cut_num += l // cut_length
    return cut_num


# input 처리
k, n = map(int, input().split())

lans = []
for _ in range(k):
    lans.append(int(input()))
### array = [int(input())for _ in range (N)] : 리스트 컴프리헨션 가능


# p.s.
start, end = 0, (2**31 - 1)
### end = max(array)로 해도 될 듯


while start <= end:
    length = (start + end) // 2
    num = get_lan_num(length)

    print(start, end, length, num)

    # 더 길게 자를 수 있겠다
    if num >= n:
        start = length + 1
    
    # 더 짧게 잘라야겠다
    elif num < n:
        end = length - 1

    # p.s.는 종료조건 따로 없이 끝까지 찾아봄 -> for 최적해

print(end)