def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        cur_num = phone_book[i]
        next_num = phone_book[i+1]
        
        if cur_num == next_num[:len(cur_num)]:
            return False
        
    return True