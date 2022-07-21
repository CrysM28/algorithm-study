# 프로그래머스 코테 연습
# 시간초과 난 코드... 잘 짠거 같은데 고쳐야 돼서 백업

# 길이 오름차순으로 정렬해서, 같은 길이면 pass, 더 길면 접두사인지 검사, 가장 긴 길이면 끝내기
def solution(phone_book):
    phone_book.sort(key=len)            # 길이순 정렬
    pb_len = len(phone_book)            # phone_book 원소 개수    
    longest = len(phone_book[pb_len-1]) # 중복 없으므로 제일 긴 거는 비교할 필요 X       
    
    print(phone_book)
    
    for i in range(pb_len):
        norm = len(phone_book[i])       # 비교 기준: 본인 길이
        if norm == longest:             # 가장 긴 길이면 더 비교하지 말고 끝
            return True
        
        for j in range(i + 1, pb_len):  
            if len(phone_book[j]) != norm:    # 같은 길이면 pass                          
                if(phone_book[j].startswith(phone_book[i])):    # 접두사면 False 리턴 및 종료
                    return False       

    return True    # 해당하는 경우 없으면 True