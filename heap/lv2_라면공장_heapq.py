#https://programmers.co.kr/learn/courses/30/lessons/42629
import heapq

def solution(stock, dates, supplies, k):
    count = 0
    idx = 0
    heap = []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, -supplies[i])
                idx = i+1
            else:
                break
        stock += -heapq.heappop(heap)
        count += 1
    return count

