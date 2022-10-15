# 재귀 활용 풀이

def BOJ13549():

    def c(n, k):
        # 뒤로 가는 경우는 -1밖에 불가능
        if n >= k:
            return n - k
        elif k == 1:
            return 1

        # 재귀
        elif k % 2:
            return 1 + min(c(n, k - 1), c(n, k + 1))
        else:  # k%2 == 0
            return min(k - n, c(n, k // 2))

    n, k = map(int, input().split())
    print(c(n, k))


BOJ13549()