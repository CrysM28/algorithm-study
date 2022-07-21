def solution(id_list, report, k):
    # dict 생성:
        ## warning_dict: 각 id를 신고한 유저 list를 저장
        ## mail_dict: id마다 신고 처리 메일을 받을 횟수를 저장
    warning_dict, mail_dict = dict(), dict()
    for id in id_list:
        warning_dict[id] = list()
        mail_dict[id] = 0   
    
    # report를 set에 넣어 중복 제거 후, 신고받은 유저(key)에 신고한 유저(value) 추가
    for r in set(report):
        warning_dict[r.split()[1]].append(r.split()[0])
    
    # value 개수가 k개 이상인 key일 때, value에 있는 id에게 모두 메일+1
    for key, value in warning_dict.items():
        if len(value) >= k:
            for id in value:
                mail_dict[id] += 1  
    
    # dict의 value를 list로 -> 최종 결과 
    mail_list = list(mail_dict.values())
    answer = mail_list
    return answer