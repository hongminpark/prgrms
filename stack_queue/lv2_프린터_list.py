# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    priorities = [(i, p) for i, p in enumerate(priorities)]
    
    count = 0
    while True:
        now = priorities.pop(0)
        if all(now[1] >= p[1] for p in priorities):
            count += 1
            if now[0] == location:
                return count
        else:
            priorities.append(now)
