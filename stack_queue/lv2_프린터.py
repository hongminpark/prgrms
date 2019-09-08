# https://programmers.co.kr/learn/courses/30/lessons/42587
from queue import Queue

def solution(priorities, location):
    q = Queue()
    count = 0
    for i in range(1, len(priorities)):
        q.put(i)

    max_idx = 0
    q.put(max_idx)
    while True:
        now = q.get()
        if q.qsize() == 0:
            return count + 1
        elif now == max_idx:
            count += 1
            max_idx = q.get()
            q.put(max_idx)
            if now == location:
                return count
        elif priorities[now] > priorities[max_idx]:
            max_idx = now
            q.put(now)
        else:
            q.put(now)
