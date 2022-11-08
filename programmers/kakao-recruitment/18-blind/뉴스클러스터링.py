# 2:58~2:24 / 
import re, math

def solution(str1, str2):
    # 처리: 소문자, 알파벳 외 제거
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = re.sub('[^a-z]', '', str1)
    str2 = re.sub('[^a-z]', '', str2)


    # 문자열 집합 생성
    str1_set, str2_set = [],[]

    tmp = ""
    for s in str1:
        if tmp != "":
            str1_set.append(tmp+s)
        tmp = s

    tmp = ""
    for s in str2:
        if tmp != "":
            str2_set.append(tmp+s)
        tmp = s


    # 교집합 크기 계산
    inter_size = 0
    for s in str1_set:
        if s in str2_set:
            inter_size += 1

    print(str1_set, str2_set)

    # 합집합 크기 계산
    union_set = []
    for s in str1_set:
        if s in str2_set:
            print(s)
            str2_set.remove(s)
        union_set.append(s)
    union_size = len(union_set)

    print(str1_set, str2_set)
    print(union_set)

    # 자카드 유사도 계산
    try:
        jaccard = inter_size / union_size
    except: # union_size = 0 등 나눗셈 실패 시
        jaccard = 1


    print(inter_size, union_size)
    print(jaccard)

    return math.trunc(jaccard*65536)




print(solution("FRANCE", "french"))
#print(solution("E=M*C^2", "e=m*c^2"))