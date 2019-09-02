# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    deploys = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    days = [deploys[0]]
    counts = []
    for d in deploys[1:]:
        if d <= days[0]:
            days.append(d)
        else:
            counts.append(len(days))
            days = [d]
    counts.append(len(days))
    return counts
