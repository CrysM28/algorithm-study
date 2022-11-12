def solution(bridge_length, weight, truck_weights):

    answer = 0

    cur_weight = 0
    cur_time = 0
    time = 0 

    for truck in truck_weights:
        print("truck ", truck)
        if (cur_weight + truck) < weight:
            cur_weight += truck
            print(cur_weight)
            cur_time += 1
        else:
            print("truck passing")
            time += weight - cur_time
            cur_weight = truck
            cur_time = 0


    print(time)



    return answer