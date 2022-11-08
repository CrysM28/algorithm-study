# 3:00 ~ 3:30?

a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
c =2


from collections import defaultdict 
def solution(id_list, report, k):
    result = defaultdict(list)
    answer = [0 for _ in range(len(id_list))]

    # 중복 제거
    report = set(report)

    # 리포트 작성
    for r in report:
        user, reported = r.split()
        result[reported].append(user)

    # 정지된 사용자 구하기
    banned = []
    for id in id_list:
        if len(result[id]) >= k:
            banned.append(id)

    # 신고 당사자에게 메일 보내기
    for i, id in enumerate(id_list):
        for b in banned:
            if id in result[b]:
                answer[i] += 1
    
    return answer


print(solution(a,b,c))