from collections import Counter


def solution(N, stages):
    counts = Counter(stages)
    cumulsum = [0] * N
    failure = []
    for i in range(N+1, 0, -1):
        if i == N+1:
            cumulsum[-1] += counts.get(i, 0)
            continue
        
        if i == N:
            cumulsum[i-1] += counts[i]
        else:
            cumulsum[i-1] += counts[i] + cumulsum[i] 
        
        if not cumulsum[i-1]:
            failure.append((i, 0))
        else:
            failure.append((i, - (counts[i] / cumulsum[i-1])))
    
    failure.sort(key=lambda x: (x[1], x[0]))
    answer = []
    for f in failure:
        answer.append(f[0])
    
    return answer

