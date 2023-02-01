# 5430. AC
from collections import deque
import sys

input = sys.stdin.readline

def calc():
    # False:0, True:1
    #reverse = 0
    reverse = False

    for pp in p:
        if pp == 'R':
            #reverse ^= 1
            reverse = not reverse
        else:
            if not arr:
                return "error"
            
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    return reverse


for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    arr = deque(eval(input()))

    result = calc()
    if result == "error":
        print(result)
        continue

    arr = list(arr)
    if result:
        arr = arr[::-1]

    print(str(arr).replace(" ", ""))