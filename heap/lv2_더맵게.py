# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        first = heapq.heappop(scoville)
        if len(scoville) == 0 and first < K:
            return -1
        elif first >= K:
            return count
        else:
            second = heapq.heappop(scoville)
            new = first + 2*second
            heapq.heappush(scoville, new)
            count += 1
