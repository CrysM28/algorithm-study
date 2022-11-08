# 1946. 신입 사원

for _ in range(int(input())):
    n = int(input())
    ppl = [list(map(int, input().split())) for _ in range(n)]
    
    # 서류 성적순
    ppl.sort()

    # 면접 성적이 더 높으면 합격
    pass_num = 1
    cur_rank = ppl[0][1]
    for s, m in ppl:
        if cur_rank > m:
            cur_rank = m
            pass_num += 1

    print(pass_num)