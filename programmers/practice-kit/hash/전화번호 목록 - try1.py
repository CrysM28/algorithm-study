def solution(phone_book):
    phone_book.sort()            # 숫자 오름차순으로 정렬
    
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):    # 정렬했으므로 다음 거 하나만 비교해도 됨                 
            if(phone_book[i+1].startswith(phone_book[i])):    # 접두사면 False 리턴 및 종료
                    return False       

    return True    # 해당하는 경우 없으면 True