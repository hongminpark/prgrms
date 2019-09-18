# https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    operations = [0, {N}]
    if number == int(str(N) * len(str(number))):
        return len(str(number))

    count = 1
    while count < 9:
        count += 1
        now = {int(str(N)*count)}
        for k in range(1, count):
            for x in operations[count-k]:
                for y in operations[k]:
                    if x and y:
                        tmp = {x + y, x - y, y - x, x // y, x * y}
                        if number in tmp:
                            return count
                    now |= tmp
        operations.append(now)
    return -1
