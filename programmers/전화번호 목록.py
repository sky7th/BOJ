def solution(phone_book):
    phone_book = set(phone_book)
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[0:i] in phone_book:
                return False

    return True
