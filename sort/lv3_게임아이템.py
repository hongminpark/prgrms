# https://school.programmers.co.kr/courses/10050/lessons/58673

import heapq

def solution(healths, items):

    healths = [h for h in healths
               if h - sorted(items, key=lambda x: x[1])[0][1] >= 100]
    items = [(-item[0], item[1], idx + 1) for idx, item in enumerate(items)]
    heapq.heapify(items)
    used = []
    for health in healths[::-1]:
        tmp = []
        while len(items):
            now = heapq.heappop(items)
            if health - now[1] >= 100:
                used.append(now[2])
                break
            else:
                tmp.append(now)
        items += tmp
        heapq.heapify(items)

    used.sort()
    return used
