# 1431. 시리얼 번호

# 기타의 개수
n = int(input())
# 기타 시리얼 번호
guitars = []
for _ in range(n):
    guitars.append(input())


## 1: 길이순 정렬
guitars.sort(key=len)

## 2,3: 자릿수 합, 사전순 정렬

# 자릿수 합 구하는 함수
def add_only_num(num_str):
    cur_sum = 0
    for n in num_str:
        if n.isdigit():
            cur_sum += int(n)
    return cur_sum


# 이전 길이
prev_len = 0
# 같은 길이인 시리얼 (시리얼, 자릿수 합)
same_len_list = []
# 정렬된 결과
sorted_guitars = []

for guitar in guitars:
    cur_len = len(guitar)
    # print(guitar)

    # 길이가 바뀌었을 때
    if prev_len < cur_len:
        prev_len = cur_len

        # same_len_list를 자리합,사전순으로 정렬 후 sorted에 저장
        if same_len_list:
            same_len_list.sort(key=lambda x:(x[1],x[0]))
            for g in same_len_list:
                sorted_guitars.append(g[0])
            same_len_list.clear()

        # 새로운 시리얼 길이부터 다시 저장
        cur_sum = add_only_num(guitar)
        same_len_list.append((guitar, cur_sum))

    # 같은 길이면 자릿수 합을 구해서 더해두기
    elif prev_len == cur_len:
        cur_sum = add_only_num(guitar)
        same_len_list.append((guitar, cur_sum))


    # print("samelen ", cur_len, same_len_list)
    # print("sorted ", sorted_guitars)

# 다 본 뒤에 same_len_list가 남았으면 더해주기
if same_len_list:
    same_len_list.sort(key=lambda x:(x[1],x[0]))
    for g in same_len_list:
        sorted_guitars.append(g[0])
    


print(*sorted_guitars, sep='\n')

