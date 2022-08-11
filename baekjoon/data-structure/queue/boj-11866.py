# 11866. 요세푸스 문제 0
## 분류: 자료구조, 큐

from collections import deque
n, k = map(int, input().split())
peoples = deque([x for x in range(1, n+1)])
tmp = k
josephus = ["<"]

# 입력 배열이 빌 때까지 반복
while peoples:
    # k번째가 되면 큐에서 삭제하고 요세푸스에 추가
    if tmp == 1:
        josephus.append(peoples.popleft())
        josephus.append(", ")
        tmp = k
    # k번째가 아니면 큐의 뒤쪽으로 보내기
    else:
        peoples.append(peoples.popleft())
        tmp -= 1

# 마무리 처리 (마지막 쉼표 제거, 꺾쇠 추가)
josephus.pop()  
josephus.append(">")

# 출력 형식
for j in josephus:
    print(j, end="")