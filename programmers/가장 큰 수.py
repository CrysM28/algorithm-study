def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key = len, reverse = True)

    print(numbers)
    max_len = len(numbers[0])
    
    
    for_sort = []
    for_addup = dict()

    for idx, number in enumerate(numbers):
        cur_len = len(number)

        new_num = number
        while cur_len < max_len:
            new_num += number[0]
            cur_len += 1

        while new_num in for_addup:
            new_num += number[0]
        
        for_addup[new_num] = number
        for_sort.append(new_num)
    
    for_sort.sort(reverse=True)

    
    # print(for_addup)
    # print(for_sort)



    answer = ''
    for nums in for_sort:
        answer += for_addup[nums]
    
    print(answer)

    return answer


