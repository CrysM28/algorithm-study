# 5525. IOIOI
## 50점
from collections import defaultdict

n = int(input())
m = int(input())
s = input()

pn_len = (n * 2) + 1

# pn 포함 개수
cnt = 0

# pn 체크
check = defaultdict(list)
del_list = []
for idx, ss in enumerate(s):
    # pn 체크
    for i,c in check.items():
        # 번갈아 나와야 pn
        if c[0] != ss:
            check[i][0] = ss
            check[i][1] += 1

        # pn 아니면 삭제
        else:
            del_list.append(i)
        
        # pn 완성
        if c[1] == pn_len:
            cnt += 1
            del_list.append(i)

    # 삭제할 거 삭제
    for d in del_list:
        del check[d]
    del_list.clear()


    # I면 일단 담기
    if ss == 'I':
        check[idx].append('I')
        check[idx].append(1)


print(cnt)