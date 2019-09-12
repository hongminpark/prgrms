#https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    times = []
    schedule = []
    end, idx = 0, 0
    while True:
        for i in range(idx, len(jobs)):
            if jobs[i][0] <= end:
                heapq.heappush(schedule, (jobs[i][1], jobs[i][0]))
                idx = i + 1
            else:
                break
        if len(schedule) == 0:
            end = jobs[idx][0]
            continue
        job = heapq.heappop(schedule)
        times.append(job[0] + (end - job[1]))
        end += job[0]
        
        if len(times) == len(jobs):
            return sum(times) // len(times)
