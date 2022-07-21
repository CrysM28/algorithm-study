from math import ceil

def solution(progresses, speeds):
    num = len(progresses)   # 작업 개수
    
    # 각 작업별로 완성에 걸리는 일 수 
    complete = list()          
    for i in range(num):
        complete.append(ceil((100 - progresses[i]) / speeds[i]))         
    
    # 앞부터 순서대로 배포
    deploy_list = list()    # 기능 배포 수 list
    progress_today = complete[0]      # 그 날 배포기능의 최대 작업일
    deploy_today = 1        # 그 날 배포한 기능 수
    
    for i in range(1, num):
        # 같이 배포할 기능이 더 없음
        if progress_today < complete[i]:
            progress_today = complete[i]
            deploy_list.append(deploy_today)
            deploy_today = 1
        # 같이 배포할 기능이 더 있음
        else:
            deploy_today += 1
    # 마지막 
    deploy_list.append(deploy_today)   

    return deploy_list