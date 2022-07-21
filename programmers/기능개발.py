        if complete[i] < complete[i+1]:
            deploy_list.append(deploy_today)
            deploy_today = 0

            
        # 뒤의 것이 완성되어 있으면 같이 배포
        j = 0
        while complete[i] >= complete[i+j] and i+j < num-1:
            print(i, j, num)
            #deploy_list.append(deploy_today)
            #deploy_today = 0
            j += 1
    