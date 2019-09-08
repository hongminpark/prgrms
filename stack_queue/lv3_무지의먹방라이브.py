from collections import deque

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = deque([i for i in range(len(food_times))]) 
    count = 0
        
    for k_ in range(k):
        if not len(q):
            return -1
        now = q.popleft()
        if food_times[now] >= 2:
            food_times[now] -= 1
            q.append(now)
    return q.popleft() + 1
