#https://programmers.co.kr/learn/courses/30/lessons/42629
from queue import PriorityQueue

def solution(stock, dates, supplies, k):
    count = 0
    idx = 0
    pq = PriorityQueue()
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                pq.put((-supplies[i], dates[i]))
                idx = i+1
            else:
                break
        stock += -pq.get()[0]
        count += 1
    return count
