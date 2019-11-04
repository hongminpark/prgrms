# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    users = {}
    results = []
    for r in record:
        r = r.split(" ")
        if r[0] == "Enter":
            users[r[1]] = r[2]
            results.append((1, r[1]))
        elif r[0] == "Leave":
            results.append((0, r[1]))
        else:
            users[r[1]] = r[2]
    prints = ["님이 나갔습니다.", "님이 들어왔습니다."]
    answer = []
    for result in results:
        answer.append(users[result[1]] + prints[result[0]])

    return answer

