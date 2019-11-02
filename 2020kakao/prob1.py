# https://programmers.co.kr/learn/courses/30/lessons/60057#

def solution(s):
    N = len(s)
    results = []
    if len(s) <= 2:
        return len(s)
    
    for k in range(1, N//2+1):
        i = 0
        s_ = ""
        stack = [s[i:i+k]]
        while True:
            i += k
            now = s[i:i+k]
            if stack[-1] == now:
                stack.append(now)
            elif len(stack) == 1:
                s_ += stack[-1]
                stack = [now]
            else:
                s_ += str(len(stack)) + stack[-1]
                stack = [now]
            if i > N - k:
                s_ += stack[-1]
                break
        results.append(len(s_))
    
    return min(results)
