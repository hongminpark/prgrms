def solution(begin, target, words):
    if target not in set(words):
        return 0
    
    conver = {}
    for a in words:
        conver.setdefault(a, [])
        for b in words:
            if convertible(a, b):
                conver[a].append(b)
    stack = [word for word in words if convertible(begin, word)]
    path = []
    answer = 100
    while stack:
        now = stack.pop()
        if now == target:
            answer = len(path)
        elif len(path) >= answer:
            path.pop()
        else:
            path.append(now)
            stack += [k for k in conver[now] if k not in path]
    if answer == 100:
        answer = 0
    return answer   

def convertible(a, b):
    if sum([a_ != b_ for a_, b_ in zip(a, b)]) == 1:
        return True
    else:
        return False
