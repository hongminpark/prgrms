#https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    clothes_dict = {}
    for name, kind in clothes:
        clothes_dict.setdefault(kind, [])
        clothes_dict[kind].append(name)

    answer = 1
    for k, v in clothes_dict.items():
        answer *= len(v) + 1
    return answer - 1
