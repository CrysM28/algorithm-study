# 이분탐색? 매개변수 탐색?으로 

import sys

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
sortList = set(numList)
sortList = sorted(list(sortList))


def lower_bound(target):
    global sortList
    left = 0
    right = len(sortList) - 1

    while left <= right:
        mid = (left + right) // 2
        if sortList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search(target):
    global sortList
    global N
    left = 0
    right = len(sortList) - 1
    while left <= right:
        mid = (left + right) // 2
        if sortList[mid] == target:
            return mid
        if sortList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


for i in numList:
    print(binary_search(i), end=" ")
