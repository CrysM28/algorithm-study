# 1
## 수학, brute-force

## 풀이 인터넷 참고
# 1로 이루어진 n의 배수 중 가장 작은 수의 자리수를 반환

while True:
    # 숫자 아니면 종료
    try:
        n = int(input())
    except:
        break   

    # 굳이 일일이 검사할 필요 없이, 1, 11, 111을 순서대로 만들어 비교하면 훨씬 빠르다.
    num = 0
    i = 1
    while True :
        num = num * 10 + 1
        num %= n
        if num == 0 :
            print(i)
            break
        i+=1

