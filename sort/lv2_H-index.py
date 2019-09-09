# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True)
    h = len(citations)
    while True:
        if h == 0:
            return 0
        count = 0
        for c in citations:
            if c >= h and count == h:
                return h
            elif c >= h:
                count += 1
            elif c < h:
                h -= 1
                break
