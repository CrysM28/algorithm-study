## 곱집합 활용

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))

    #print(l)
    #print(list(product(*l)))

    return s.count(target)

print(solution([4,1,2,1], 4))

