import sys


def solution(arr):
    n = len(arr)
    ans = 1
    for i in range(n):
        cnt = 1

        # 가로
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt

        cnt = 1
        # 세로
        for j in range(1, n):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans


if __name__ == '__main__':
    read = sys.stdin.readline
    arr = []
    answer = 0
    n = int(read())
    for i in range(n):
        arr.append(list(map(str, read().rstrip())))

    for i in range(n):
        for j in range(n):
            # 열 바꾸기
            if j + 1 < n:
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                temp = solution(arr)
                if temp > answer:
                    answer = temp
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            # 행 바꾸기
            if i + 1 < n:
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                temp = solution(arr)
                if temp > answer:
                    answer = temp
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

    print(answer)
