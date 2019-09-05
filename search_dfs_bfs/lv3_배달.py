# https://programmers.co.kr/learn/courses/30/lessons/12978
from queue import Queue

def solution(N, road, K):
    dist = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for a, b, c in road:
        if not dist[a][b]:
            dist[a][b] = dist[b][a] = c
        else:
            dist[a][b] = dist[b][a] = min(dist[a][b], c)
    q = Queue()
    q.put(1)
    visited = [0] * (N+1)
    while q.qsize():
        now = q.get()
        for k in range(2, N+1):
            if not visited[k] and dist[now][k] \
                and visited[now] + dist[now][k] <= K:
                visited[k] = visited[now] + dist[now][k]
                q.put(k)
    return sum([1 for _ in visited if 0 < _ <= K]) + 1
