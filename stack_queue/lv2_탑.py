# https://programmers.co.kr/learn/courses/30/lessons/42588
def solution(heights):
    answer = [0] * len(heights)
    while heights:
        beam = heights.pop()
        for idx, left in enumerate(heights[::-1]):
            if left > beam:
                answer[len(heights)] = len(heights) - idx
                break
    return answer
