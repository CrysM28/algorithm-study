# 1920. 수 찾기
## 이분탐색 풀이: pypy3 244ms -> 비슷하거나 느림

n_num = int(input())
n_list = list(map(int, input().split()))
m_num = int(input())
m_list = list(map(int, input().split()))

# 정렬 후
n_list.sort()

# 이분탐색
for m in m_list:
    answer = 0
    start, end = 0, n_num - 1

    # 범위 안인지 먼저 체크
    if m < n_list[start] or m > n_list[end]:
        print(answer)
        continue

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] < m:
            start = mid + 1
        elif n_list[mid] > m:
            end = mid - 1
        else:   
            answer = 1
            break
    
    print(answer)


# 10816과 같은 풀이로 가능할까? -> 가능
## set 이용한 풀이: pypy3 240ms

# n = int(input())
# sg_cards = set(input().split())
# m = int(input())
# input_cards = list(input().split())

# for c in input_cards:
#     if c in sg_cards:
#         print(1)
#     else:
#         print(0)
