def solution(n, computer):
    answer = 0
    visited = [0] * n
    
    for from_ in range(n):
        if not visited[from_]:
            stack = [to_ for to_ in range(n) if computer[from_][to_] == 1]
            while stack:
                now = stack.pop()
                if not visited[now]:
                    stack += [to_ for to_ in range(n) if computer[now][to_] == 1]
                    visited[now] = 1
            answer += 1
    return answer
