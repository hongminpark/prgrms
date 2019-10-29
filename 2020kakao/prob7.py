# https://programmers.co.kr/learn/courses/30/lessons/60063

def solution(board):
    N = len(board)
    stack = [(0, 0, 0)]
    visited = []

    while stack:
        print(visited)
        now = stack.pop()
        x, y, s = now[0], now[1], now[2]

        if now == (N - 2, N - 1, 1) or now == (N - 1, N - 2, 0):
            return len(visited)

        # 가로일때
        nexts = []
        if s == 0:
            if y + 2 < N and not board[x][y + 2]:
                nexts.append((x, y + 1, 0))
            if x + 1 < N and y + 1 < N and \
                    not board[x + 1][y] and not board[x + 1][y + 1]:
                nexts.append((x, y+1, 1))
            if not nexts:
                visited.pop()
            else:
                visited.append(now)
                stack += nexts
        # 세로일때
        else:
            if x + 2 < N and not board[x + 2][y]:
                nexts.append((x + 1, y, 1))
            if x + 1 < N and y + 1 < N and \
                    not board[x][y + 1] and not board[x + 1][y + 1]:
                nexts.append((x + 1, y, 0))
            if not nexts:
                visited.pop()
            else:
                visited.append(now)
                stack += nexts

if __name__ == "__main__":
    # solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
    solution([[0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
            
