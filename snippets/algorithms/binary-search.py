# 재귀
def binary_search_recursive(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, end)

    # 찾은 경우 중간점 인덱스 반환
    else:
        return mid


# 반복
def binary_search_iterative(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    
    # 못 찾음
    return -1


# 이진 검색 모듈
import bisect

def binary_search_bisect(array, target):
    index = bisect.bisect_left(array, target)

    if index < len(array) and array[index] == target:
        return index
    else:
        return -1