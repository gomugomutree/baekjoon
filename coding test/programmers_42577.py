def solution(phone_book):
    # phone_book.sort(key=len)
    phone_book.sort()
    
    
    for phone1, phone_other in zip(phone_book, phone_book[1:]):
        # print(phone1, phone_other)
        if phone_other.startswith(phone1):
            return False
        
    return True