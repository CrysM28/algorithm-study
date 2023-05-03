# 17088. 등차수열 변환

def is_same(a):
    for e in a[1:]:
        if e != a[0]:
            return False
    return True


def backtrack(array):
    if len(array) == N:
        return
    

    for i in range(0, -1, 1):
        





N = int(input())
arr = list(map(int, input().split()))

cnt = 0

diff = []

for i in range(N-1):
    diff.append(arr[i+1]-arr[i])

print(diff)

print(is_same(diff))
