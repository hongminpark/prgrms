#https://programmers.co.kr/learn/courses/30/lessons/42628
def solution(operations):
    result = []
    for operation in operations:
        a, b = operation.split(" ")
        if a == "I":
            result.append(int(b))
            result.sort()
        elif a == "D" and len(result) > 0:
            if b == "1":
                result = result[:-1]
            else:
                result = result[1:]

    if len(result) == 0:
        return [0, 0]
    elif len(result) == 1:
        return [result[0], result[0]]
    else:
        return [result[-1], result[0]]
