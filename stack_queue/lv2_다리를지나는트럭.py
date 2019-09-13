#https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    dq = deque([0] * bridge_length)
    for truck in truck_weights:
        while True:
            dq.popleft()
            time += 1
            if truck <= weight - sum(dq):
                dq.append(truck)
                break
            else:
                dq.append(0)
    while len(dq):
        dq.popleft()
        time += 1
    
    return time
