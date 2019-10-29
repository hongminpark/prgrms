# https://programmers.co.kr/learn/courses/30/lessons/60063

def solution(board):
    N = len(board)
    stack = [(0, 0, 0)]
    visited = []
    
    while stack:
        now = stack.pop()
        print(now)
        x, y, s = now[0], now[1], now[2]
        visited.append(now)
        
        if now is (N-2, N-1, 1) or now is (N-1, N-2, 0):
            return len(visited)
        
        # 가로일때
        if s == 0:
            if y+2 < N and not board[x][y+2]:
                stack.append((x, y+1, 0))
            if x+1 < N and y+1 < N and \
                not board[x+1][y] and not board[x+1][y+1]:
                stack.append((x, y, 1))
        # 세로일때
        else:
            if x+2 < N and not board[x+2][y]:
                stack.append((x+1, y, 0))
            if x+1 < N and y+1 < N and \
            not board[x][y+1] and not board[x+1][y+1]:
                stack.append((x+1, y, 0))

if __name__ == "__main__":
    solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
            
