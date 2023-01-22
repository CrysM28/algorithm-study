# 2775. 부녀회장이 될테야

# (층, 호)
def resident(i, j):
    # 종료조건
    if i == 0:
        return j
    elif j == 1:
        return 1

    # 재귀
    return resident(i - 1, j) + resident(i, j - 1)


t = int(input())
for _ in range(t):
    k, n = int(input()), int(input())
    print(resident(k, n))


## 이 문제는 입력이 작아서 (1~14) 배열로 만들고 찾는 편이 빨랐을지도
### 실험결과 실제로 그렇습니다 (2116 -> 112)
