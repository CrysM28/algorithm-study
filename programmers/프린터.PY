# 최대힙 구현이면 간단하게 될듯
# 순서를 알아야하므로 노드를 (값, 위치)인 list로 저장

# 쓸데없는 짓 하다가 시간 버림....
# 그래도 최대힙 직접 구현은 했네요

def solution(priorities, location):
    
    print(max_heap(priorities))
    
    
    
    
    answer = 0
    return answer


# 리스트 형태를 
def max_heap(list_unsorted):
    mheap = [0]     # leave index 0 empty   
    
    for i in range(len(list_unsorted)):
        mheap.append(list_unsorted[i])  # 일단 끝에 넣고  
        mindex = i+1
        while (mindex // 2) != 0:       # 부모 노드와 비교해서 크면 교환, 아니면 break
            if mheap[mindex] > mheap[mindex//2]:
                mheap[mindex], mheap[mindex//2] = mheap[mindex//2], mheap[mindex]
            else:
                break
            mindex = mindex // 2        # 성공 시 계속 부모 노드 찾아 교환
            
    return mheap
    