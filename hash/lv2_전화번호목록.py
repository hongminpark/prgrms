# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    phone_book.sort()
    for p_ in phone_book:
        for p__ in phone_book:
            if p_ != p__ and p__.startswith(p_):
                return False
    return True

