# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
def solution(n, edge):
    routes = dict()
    for e in edge:
        routes.setdefault(e[0], [])
        routes.setdefault(e[1], [])
        routes[e[0]].append(e[1])
        routes[e[1]].append(e[0])

    visited = [0] * (n+1)
    visited[1] = 1
    stack = [1]
    lastnode = len(stack)
    while True:
        tmp = []
        for now in stack:
            for n in routes[now]:
                if not visited[n]:
                    visited[n] = 1
                    tmp.append(n)
        if tmp:
            stack = tmp
        else:
            return len(stack)
