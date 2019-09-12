#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    pattern = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0] * 3
    for i, ans in enumerate(answers):
        for k in range(3):
            count[k] += (ans == pattern[k][i%len(pattern[k])])
    return [i+1 for i, v in enumerate(count) if v == max(count)]
