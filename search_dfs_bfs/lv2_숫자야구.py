#https://programmers.co.kr/learn/courses/30/lessons/42841
from itertools import permutations

def solution(baseball):
    lists = permutations([str(i) for i in range(1, 10)], 3)
    lists = ["".join(i) for i in lists]

    for n, s, b in baseball:
        lists_ = []
        n = str(n)
        for item in lists:
            s_, b_ = 0, 0
            n_ = set(n)
            for i in range(3):
                if item[i] == n[i]:
                    s_ += 1
                elif item[i] in n_:
                    b_ += 1
            if (s_, b_) == (s, b):
                lists_.append(item)
        lists = lists_
    return len(lists)
