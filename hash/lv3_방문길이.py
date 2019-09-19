# https://school.programmers.co.kr/courses/10050/lessons/58669

def solution(dirs):
    deltas = {"U": (0, 1),
             "D": (0, -1),
             "R": (1, 0),
             "L": (-1, 0)}
    visited = set()
    start = (0, 0)
    for d in dirs:
        move = (start[0] + deltas[d][0], start[1] + deltas[d][1])
        if not max(abs(move[0]), abs(move[1])) > 5:
            if ((start, move) or (move, start)) not in visited:
                visited.add((start, move))
            start = move
    return len(visited)
