# 프로그래머스 코테 연습
# 시간초과 난 코드... 다시 고칠것
def solution(id_list, report, k):
    # dict 생성:
        ## warning_dict: id마다 신고받은 횟수 저장
        ## mail_dict: id마다 신고 처리 메일을 받을 횟수 저장
    warning_dict = dict()    
    mail_dict = dict()    
    for id in id_list:
        warning_dict[id] = 0
        mail_dict[id] = 0
    
    # 중복 신고 처리를 위해 report에서 중복된 문자열을 제거 후 신고받은 횟수 계산
    ## list를 set에 넣어 중복 제거
    report_set = set(report)
    for r in report_set:
        warning_dict[r.split()[1]] += 1

    # 정지된 유저가 있으면, report_set에서 정지 유저를 신고한 유저의 메일 횟수 증가시키기
    for key, value in warning_dict.items():
        if(value >= k):
            for r in report_set:
                if(r.split()[1] == key):
                    mail_dict[(r.split()[0])] += 1
    
    # dict의 value만을 list로 변경하여 최종 결과 출력
    mail_list = list(mail_dict.values())
                    
    answer = mail_list
    #print(answer)
    return answer
