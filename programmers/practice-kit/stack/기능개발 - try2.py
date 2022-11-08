def solution(progresses, speeds):
    deploy = []

    end = []
    for progress, speed in zip(progresses, speeds):
        days, remainder = divmod(100 - progress, speed)
        if remainder != 0:
            days += 1
        end.append(days)


    last_deploy = end[0]
    deploy_num = 0
    for e in end:
        if e <= last_deploy:
            deploy_num += 1
        else:
            last_deploy = e
            deploy.append(deploy_num)
            deploy_num = 1

    if deploy_num != 0:
        deploy.append(deploy_num)

    return deploy