from collections import OrderedDict

def solution(priorities, location):
    answer = 0
    index_arr = [c for c in range(len(priorities))] # index 위치 저장 
    
    i = 0
    while True:
        if priorities[i] < max(priorities[i+1:]):
            index_arr.append(index_arr.pop(i))
            priorities.append(priorities.pop(i))
        else:
            i += 1

        if priorities == sorted(priorities, reverse=True):
            break

    return index_arr.index(location) + 1

